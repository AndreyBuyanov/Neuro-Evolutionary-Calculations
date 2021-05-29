from typing import List
import numpy as np
from .neuron import Neuron
from .layer import Layer
from .activations import Sigmoid


class NeuralNetwork(object):
    def __init__(self, hidden_neurons: List[Neuron], inputs_count: int, outputs_count: int):
        self.input_weights = np.zeros((len(hidden_neurons), inputs_count))
        self.output_weights = np.zeros((outputs_count, len(hidden_neurons)))
        for i in range(len(hidden_neurons)):
            self.input_weights[i] = hidden_neurons[i].get_input_weights(inputs_count)
            self.output_weights[i] = hidden_neurons[i].get_output_weights(outputs_count)
        self.layers = []
        self.layers.append(
            Layer(weights=self.input_weights, activation=Sigmoid()))
        self.layers.append(
            Layer(weights=self.output_weights, activation=Sigmoid()))

    def forward(self, input_data: np.array) -> np.array:
        output = input_data
        for layer in self.layers:
            output = layer.forward(output)
        return output
