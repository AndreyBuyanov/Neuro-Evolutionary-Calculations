import os
import numpy as np


def transform_data(dataset, inputs, outputs):
    input_data = np.zeros((len(dataset), inputs))
    output_data = np.zeros((len(dataset), outputs))
    for i in range(len(dataset)):
        data = [float(value) for value in dataset[i].split(' ')]
        input_data[i] = data[:inputs]
        output_data[i] = data[inputs:]
    return input_data, output_data


def load(path):
    with open(path, 'r') as f:
        lines = f.readlines()

        bool_in = int(lines[0].split('=')[1])
        real_in = int(lines[1].split('=')[1])
        bool_out = int(lines[2].split('=')[1])
        real_out = int(lines[3].split('=')[1])
        training_examples_count = int(lines[4].split('=')[1])
        validation_examples_count = int(lines[5].split('=')[1])
        test_examples_count = int(lines[6].split('=')[1])

        inputs = bool_in + real_in
        outputs = bool_out + real_out

        current_line = 7
        train_x, train_y = transform_data(lines[current_line:current_line + training_examples_count], inputs, outputs)
        current_line += training_examples_count
        validation_x, validation_y = transform_data(lines[current_line:current_line + validation_examples_count], inputs, outputs)
        current_line += validation_examples_count
        test_x, test_y = transform_data(lines[current_line:current_line + test_examples_count], inputs, outputs)

        return train_x, train_y, validation_x, validation_y, test_x, test_y


class AbstractDataset(object):
    def __init__(self, path):
        self.train_x, self.train_y, self.validation_x, self.validation_y, self.test_x, self.test_y = load(path)

    def get_train_data(self):
        return self.train_x, self.train_y

    def get_validation_data(self):
        return self.validation_x, self.validation_y

    def get_test_data(self):
        return self.test_x, self.test_y


class Cancer1Dataset(AbstractDataset):
    def __init__(self):
        super().__init__(os.path.dirname(__file__) + '/data/cancer1.dt')


class Cancer2Dataset(AbstractDataset):
    def __init__(self):
        super().__init__(os.path.dirname(__file__) + '/data/cancer2.dt')


class Cancer3Dataset(AbstractDataset):
    def __init__(self):
        super().__init__(os.path.dirname(__file__) + '/data/cancer3.dt')


class Diabetes1Dataset(AbstractDataset):
    def __init__(self):
        super().__init__(os.path.dirname(__file__) + '/data/diabetes1.dt')


class Diabetes2Dataset(AbstractDataset):
    def __init__(self):
        super().__init__(os.path.dirname(__file__) + '/data/diabetes2.dt')


class Diabetes3Dataset(AbstractDataset):
    def __init__(self):
        super().__init__(os.path.dirname(__file__) + '/data/diabetes3.dt')


class Glass1Dataset(AbstractDataset):
    def __init__(self):
        super().__init__(os.path.dirname(__file__) + '/data/glass1.dt')


class Glass2Dataset(AbstractDataset):
    def __init__(self):
        super().__init__(os.path.dirname(__file__) + '/data/glass2.dt')


class Glass3Dataset(AbstractDataset):
    def __init__(self):
        super().__init__(os.path.dirname(__file__) + '/data/glass3.dt')
