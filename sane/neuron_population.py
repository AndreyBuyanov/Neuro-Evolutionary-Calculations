from .neuron import Neuron


class NeuronPopulation(object):
    def __init__(self, population_size: int, connections_count: int):
        self.neurons = []
        for i in range(population_size):
            self.neurons.append(Neuron(
                connections_count=connections_count, neuron_id=i))

    def init(self, min_value: float, max_value: float):
        for i in range(len(self.neurons)):
            self.neurons[i].init(
                min_value=min_value,
                max_value=max_value)

    def sort(self):
        self.neurons.sort(key=lambda x: x.fitness)

    def __getitem__(self, key: int) -> Neuron:
        return self.neurons[key]

    def __len__(self):
        return len(self.neurons)
