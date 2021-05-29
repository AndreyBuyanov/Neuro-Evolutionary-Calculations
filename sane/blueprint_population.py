from typing import List
import random
from .blueprint import Blueprint
from .neuron_population import NeuronPopulation
from .neuron import Neuron


class BlueprintPopulation(object):
    def __init__(self, population_size: int, blueprint_size: int):
        self.population_size = population_size
        self.blueprint_size = blueprint_size
        self.blueprints = []

    def init(self, neuron_population: NeuronPopulation):
        for i in range(self.population_size):
            selected_neurons = self.select_neurons(
                neuron_population=neuron_population)
            self.blueprints.append(Blueprint(selected_neurons))

    def select_neurons(self, neuron_population: NeuronPopulation) -> List[Neuron]:
        result = []
        while True:
            for i in range(self.blueprint_size):
                result.append(random.choice(seq=neuron_population))
            neuron_identifiers = [neuron.id for neuron in result]
            if len(set(neuron_identifiers)) == self.blueprint_size:
                break
            result.clear()
        return result

    def reset_neurons_fitness(self):
        for i in range(len(self.blueprints)):
            self.blueprints[i].reset_neurons_fitness()

    def __getitem__(self, key: int) -> Blueprint:
        return self.blueprints[key]

    def __len__(self):
        return len(self.blueprints)
