class MultpileOfFiveSet:

    def __init__(self):
        self.inner_set = set()

    def filter_condition(self, element):
        return element % 5 == 0

    def put(self, element):
        if self.filter_condition(element):
            self.inner_set.add(element)

    def get(self):
        return self.inner_set
