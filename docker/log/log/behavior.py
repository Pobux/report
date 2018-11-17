
class Behavior:

    def __init__(self, strategy):
        self._strategy = strategy

    def create_log(self):
        self._strategy.create_log()


class TextLog(Behavior):

    def create_log(self):
        print("Text log create")


class GraphLog(Behavior):

    def create_log(self):
        print("Graph log create")
