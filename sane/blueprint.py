from typing import List
from .neuron import Neuron


class Blueprint(object):
    def __init__(self, neurons: List[Neuron]):
        self.neurons = neurons

    def reset_neurons_fitness(self):
        for i in range(len(self.neurons)):
            self.neurons[i].reset_fitness()
