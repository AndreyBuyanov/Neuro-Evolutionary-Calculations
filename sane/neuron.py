import numpy as np
from .gene import Gene, ConnectionType


class Neuron(object):
    def __init__(self, connections_count: int, neuron_id: int):
        self.genes = []
        self.connections_count = connections_count
        self.neuron_id = neuron_id
        self.fitness = 0.0

    def init(self, min_value: float, max_value: float):
        while True:
            for i in range(self.connections_count):
                self.genes.append(Gene(
                    min_value=min_value,
                    max_value=max_value))
            for i in range(self.connections_count):
                self.genes[i].init()
            connection_types = [connection.get_connection_type().value for connection in self.genes]
            if len(set(connection_types)) > 1:
                break

    def get_weights(self, neurons_count: int, connection: ConnectionType) -> np.array:
        result = np.zeros(neurons_count)
        for gene in self.genes:
            if gene.get_connection_type() == connection:
                result[gene.get_index(neurons_count)] = gene.get_weight()
        return result

    def get_input_weights(self, neurons_count: int) -> np.array:
        return self.get_weights(
            neurons_count=neurons_count,
            connection=ConnectionType.INPUT)

    def get_output_weights(self, neurons_count: int) -> np.array:
        return self.get_weights(
            neurons_count=neurons_count,
            connection=ConnectionType.OUTPUT)

    def reset_fitness(self):
        self.fitness = 0.0

    def get_id(self) -> int:
        return self.neuron_id
    id = property(get_id)
