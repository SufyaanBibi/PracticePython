class FiFoQ(list):

    def enqueue(self, e):
        self.append(e)

    def dequeue(self):
        return self.pop(0)
