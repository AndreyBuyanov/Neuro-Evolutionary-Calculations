from .blueprint import Blueprint


class Blueprints(object):
    def __init__(self, blueprints_count: int, neurons_count: int, connections_count: int):
        self.blueprints = [None] * blueprints_count
        for i in range(blueprints_count):
            self.blueprints[i] = Blueprint(
                neurons_count=neurons_count,
                connections_count=connections_count)

    def init(self, min_value: float, max_value: float):
        for i in range(0, len(self.blueprints)):
            self.blueprints[i].init(
                min_value=min_value,
                max_value=max_value)
