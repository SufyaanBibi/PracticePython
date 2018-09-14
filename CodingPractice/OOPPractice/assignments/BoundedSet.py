class BoundedSet:

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.inner_set = set()

    def put(self, element):
        if self.filter_condition(element):
            self.inner_set.add(element)

    def filter_condition(self, element):
        return element >= self.lower_bound and element <= self.upper_bound

    def get(self):
        return self.inner_set
