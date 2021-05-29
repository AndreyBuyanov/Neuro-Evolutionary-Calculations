from enum import Enum
import random


class ConnectionType(Enum):
    INPUT = 1
    OUTPUT = 2

    @classmethod
    def from_label(cls, label: int):
        return cls(cls.OUTPUT if label > 127 else cls.INPUT)


class Integer16Gene(object):
    def __init__(self, value: float, min_value: float, max_value: float):
        self.float_value = value
        self.min_value = min_value
        self.max_value = max_value

    def init(self):
        self.float_value = random.uniform(self.min_value, self.max_value)

    def get_int_value(self) -> int:
        return int((self.float_value - self.min_value) * (2**16 - 1) / (self.max_value - self.min_value))

    def set_int_value(self, int_value: int):
        self.float_value = int_value * (self.max_value - self.min_value) / (2**16 - 1) + self.min_value
    int_value = property(get_int_value, set_int_value)

    def get_value(self) -> float:
        return self.float_value
    value = property(get_value)

    def mutation(self):
        mutation_bit = random.randrange(16)
        mutation_mask = (1 << mutation_bit) & (2 ** 16 - 1)
        self.int_value ^= mutation_mask

    @staticmethod
    def crossover(parent1, parent2):
        min_value = parent1.min_value
        max_value = parent1.max_value
        crossover_point = random.randrange(16)
        mask1 = ((2**16 - 1) << crossover_point) & (2**16 - 1)
        mask2 = ((2**16 - 1) >> (16 - crossover_point)) & (2**16 - 1)
        child1_gene = (parent1.int_value & mask1) | (parent2.int_value & mask2)
        child2_gene = (parent2.int_value & mask1) | (parent1.int_value & mask2)
        child1 = Integer16Gene(value=0.0, min_value=min_value, max_value=max_value)
        child2 = Integer16Gene(value=0.0, min_value=min_value, max_value=max_value)
        child1.int_value = child1_gene
        child2.int_value = child2_gene
        return child1, child2


class Gene(object):
    def __init__(self, min_value: float, max_value: float):
        self.label = 0
        self.weight = Integer16Gene(0.0, min_value, max_value)

    def get_connection_type(self) -> ConnectionType:
        return ConnectionType.from_label(self.label)

    def get_index(self, neurons_count) -> int:
        return self.label % neurons_count

    def get_weight(self) -> float:
        return self.weight.value

    def init(self):
        self.label = int(random.random() * (2**8 - 1))
        self.weight.init()

    def mutation(self):
        if random.random() <= 0.001:
            mutation_bit = random.randrange(8)
            mutation_mask = (1 << mutation_bit) & (2 ** 8 - 1)
            self.label ^= mutation_mask
            self.weight.mutation()

    @staticmethod
    def crossover(parent1, parent2):
        min_value = parent1.weight.min_value
        max_value = parent1.weight.max_value
        crossover_point = random.randrange(8)
        mask1 = ((2 ** 8 - 1) << crossover_point) & (2 ** 8 - 1)
        mask2 = ((2 ** 8 - 1) >> (8 - crossover_point)) & (2 ** 8 - 1)
        child1_gene = (parent1.label & mask1) | (parent2.label & mask2)
        child2_gene = (parent2.label & mask1) | (parent1.label & mask2)
        child1 = Gene(min_value=min_value, max_value=max_value)
        child2 = Gene(min_value=min_value, max_value=max_value)
        child1.label = child1_gene
        child2.label = child2_gene
        child1_weight, child2_weight = Integer16Gene.crossover(
            parent1=parent1.weight, parent2=parent2.weight)
        child1.weight = child1_weight
        child2.weight = child2_weight
        return child1, child2
