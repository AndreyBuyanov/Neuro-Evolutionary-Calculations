from .neuron import Neuron


class Blueprint(object):
    def __init__(self, neurons_count: int, connections_count: int):
        self.neurons = [None] * neurons_count
        for i in range(neurons_count):
            self.neurons[i] = Neuron(
                connections_count=connections_count)

    def init(self, min_value: float, max_value: float):
        for i in range(len(self.neurons)):
            self.neurons[i].init(
                min_value=min_value,
                max_value=max_value)

    def reset_neurons_fitness(self):
        for i in range(len(self.neurons)):
            self.neurons[i].reset_fitness()
