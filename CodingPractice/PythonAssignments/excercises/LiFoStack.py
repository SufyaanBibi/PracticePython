class LiFoStack(list):

    def push(self, element):
        self.append(element)

    def pop(self):
        return super().pop(-1)

    def peek(self):
        return self[-1]
