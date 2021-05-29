from .neuron_population import NeuronPopulation
from .blueprint_population import BlueprintPopulation


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

    def run(self, generations_count: int):
        for i in range(generations_count):
            self.blueprint_population.reset_neurons_fitness()
