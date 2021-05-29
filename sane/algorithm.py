from typing import List
import numpy as np
import random
from copy import deepcopy
from .neuron_population import NeuronPopulation
from .blueprint_population import BlueprintPopulation
from .nn import NeuralNetwork
from .utils import mse


class SANEAlgorithm(object):
    def __init__(self, blueprints_population_size: int, neuron_population_size: int, hidden_layer_size: int, connections_count: int):
        self.neuron_population = NeuronPopulation(
            population_size=neuron_population_size,
            connections_count=connections_count)
        self.blueprint_population = BlueprintPopulation(
            population_size=blueprints_population_size,
            blueprint_size=hidden_layer_size)

    def init(self, min_value: float, max_value: float):
        self.neuron_population.init(
            min_value=min_value,
            max_value=max_value)
        self.blueprint_population.init(
            neuron_population=self.neuron_population)

    def train(self, generations_count: int, x_train: np.array, y_train: np.array):
        if x_train.ndim != y_train.ndim:
            raise Exception()
        result = []
        for generation in range(generations_count):
            inputs_count = x_train[0].size
            outputs_count = y_train[0].size
            neural_networks = self.create_neural_networks(
                inputs_count=inputs_count,
                outputs_count=outputs_count)
            self.forward(
                neural_networks=neural_networks,
                x_train=x_train,
                y_train=y_train)
            neural_networks.sort(key=lambda x: x.fitness)
            best_nn = neural_networks[0]
            result.append((
                best_nn.fitness,
                deepcopy(best_nn.input_weights),
                deepcopy(best_nn.output_weights)))
            self.update_neuron_fitness()
            self.neuron_population.crossover()
            self.neuron_population.mutation()
            self.blueprint_population.crossover()
            self.blueprint_population.mutation()
        return result

    def forward(self, neural_networks: List[NeuralNetwork], x_train: np.array, y_train: np.array):
        dataset_size = x_train.shape[0]
        for i in range(len(neural_networks)):
            data_index = random.randrange(dataset_size)
            output = neural_networks[i].forward(x_train[data_index])
            error = mse(y_train[data_index], output)
            neural_networks[i].fitness = error
            self.blueprint_population[i].fitness = error

    def create_neural_networks(self, inputs_count: int, outputs_count: int) -> List[NeuralNetwork]:
        result = []
        for i in range(len(self.blueprint_population)):
            hidden_neurons = self.blueprint_population[i].neurons
            result.append(NeuralNetwork(
                hidden_neurons=hidden_neurons,
                inputs_count=inputs_count,
                outputs_count=outputs_count,
                neuron_population=self.neuron_population))
        return result

    def update_neuron_fitness(self):
        for i in range(len(self.neuron_population)):
            fitness_list = []
            for j in range(len(self.blueprint_population)):
                if i in self.blueprint_population[j].neurons:
                    fitness_list.append(self.blueprint_population[j].fitness)
                if len(fitness_list) == 5:
                    break
            self.neuron_population[i].fitness = np.array(fitness_list).mean() if len(fitness_list) > 0 else 0.0
