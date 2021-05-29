from typing import List
from .neuron_population import NeuronPopulation
from .blueprint_population import BlueprintPopulation
from .nn import NeuralNetwork


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

    def run(self, generations_count: int, inputs_count: int, outputs_count: int):
        for generation in range(generations_count):
            self.blueprint_population.reset_neurons_fitness()
            neural_networks = self.create_neural_networks(
                inputs_count=inputs_count,
                outputs_count=outputs_count)

    def create_neural_networks(self, inputs_count: int, outputs_count: int) -> List[NeuralNetwork]:
        result = []
        for i in range(len(self.blueprint_population)):
            hidden_neurons = self.blueprint_population[i].neurons
            result.append(NeuralNetwork(
                hidden_neurons=hidden_neurons,
                inputs_count=inputs_count,
                outputs_count=outputs_count))
        return result
