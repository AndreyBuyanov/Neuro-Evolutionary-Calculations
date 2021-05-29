from enum import Enum
from random import random, uniform
from ctypes import c_uint8, c_uint16


class ConnectionType(Enum):
    INPUT = 1
    OUTPUT = 2

    @classmethod
    def from_label(cls, label: c_uint8):
        return cls(cls.OUTPUT if label.value > 127 else cls.INPUT)


class Integer16Gene(object):
    def __init__(self, value: float, min_value: float, max_value: float):
        self.float_value = value
        self.min_value = min_value
        self.max_value = max_value

    def init(self):
        self.float_value = uniform(self.min_value, self.max_value)

    def get_int_value(self) -> c_uint16:
        return c_uint16(int((self.float_value - self.min_value) * (2**16 - 1) / (self.max_value - self.min_value)))

    def set_int_value(self, int_value: c_uint16):
        self.float_value = int_value.value * (self.max_value - self.min_value) / (2**16 - 1) + self.min_value
    int_value = property(get_int_value, set_int_value)

    def get_value(self) -> float:
        return self.float_value
    value = property(get_value)


class Gene(object):
    def __init__(self, min_value: float, max_value: float):
        self.label = c_uint8(0)
        self.weight = Integer16Gene(0.0, min_value, max_value)

    def get_connection_type(self) -> ConnectionType:
        return ConnectionType.from_label(self.label)

    def get_index(self, neurons_count) -> int:
        return self.label.value % neurons_count

    def get_weight(self) -> float:
        return self.weight.value

    def init(self):
        self.label = c_uint8(int(random() * (2**8 - 1)))
        self.weight.init()
