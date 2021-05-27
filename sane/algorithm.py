from blueprints import Blueprints


class SANEAlgorithm(object):
    def __init__(self, blueprints_count: int, neurons_count: int, connections_count: int):
        self.blueprints = Blueprints(
            blueprints_count=blueprints_count,
            neurons_count=neurons_count,
            connections_count=connections_count)

    def init(self):
        self.blueprints.init()

    def run(self, generations_count: int):
        pass
