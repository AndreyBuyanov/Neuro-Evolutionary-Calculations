from .blueprint_population import BlueprintPopulation


class SANEAlgorithm(object):
    def __init__(self, blueprints_count: int, neurons_count: int, connections_count: int):
        self.blueprint_population = BlueprintPopulation(
            blueprints_count=blueprints_count,
            neurons_count=neurons_count,
            connections_count=connections_count)

    def init(self, min_value: float, max_value: float):
        self.blueprint_population.init(min_value=min_value, max_value=max_value)

    def run(self, generations_count: int):
        for i in range(generations_count):
            self.blueprint_population.reset_neurons_fitness()
