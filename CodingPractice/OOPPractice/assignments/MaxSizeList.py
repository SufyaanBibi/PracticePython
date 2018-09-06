class MaxSizeList:

    def __init__(self, limit):
        self.__limit = limit
        self.__inner_list = []

    def push(self, value):
        self.__inner_list.append(value)
        if len(self.__inner_list) > self.__limit:
            self.__inner_list.pop(0)

    def get_list(self):
        return self.__inner_list
