class MockQueue:
    def __init__(self):
        self.queue = list()

    def get(self):
        return self.queue.pop()

    def put(self, element):
        return self.queue.append(element)
