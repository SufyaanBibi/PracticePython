class MaxSizeList:

    def __init__(self, limit):
        self.limit = limit
        self.inner_list = []

    def push(self, value):
        self.inner_list.append(value)
        if len(self.inner_list) > self.limit:
            self.inner_list.pop(0)

    def get_list(self):
        return self.inner_list
