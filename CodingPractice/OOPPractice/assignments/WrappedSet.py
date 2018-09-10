class WrappedSet:
    def __init__(self, filter_condition):
        self.inner_set = set()
        self.filter_condition = filter_condition

    def put(self, element):
        if self.filter_condition(element):
            self.inner_set.add(element)

    def get(self):
        return self.inner_set