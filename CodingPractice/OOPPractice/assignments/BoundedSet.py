class BoundedSet:

    def __init__(self, limit_1, limit_2):
        self.limit_1 = limit_1
        self.limit_2 = limit_2
        self.inner_set = set()

    def put(self, element):
        if element >= self.limit_1 and element <= self.limit_2:
            self.inner_set.add(element)
        else:
            print('Number is out of bounds.')

    def get(self):
        return self.inner_set