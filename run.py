from sane import SANEAlgorithm


def run():
    algorithm = SANEAlgorithm(2, 4, 2, 2)
    algorithm.init(-1.0, 1.0)
    algorithm.run(2)


run()
