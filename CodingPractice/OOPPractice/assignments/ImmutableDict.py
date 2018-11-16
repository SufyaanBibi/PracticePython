from CodingPractice.OOPPractice.assignments.CustomException import SetAttributeError, DeleteAttributeError


class ImmutableDict(dict):

    def __init__(self, tuple_elements):
        dict.__init__(self)
        for key, value in tuple_elements:
            dict.__setitem__(self, key, value)

    def __setitem__(self, key, value):
        return

    def __delitem__(self, key):
        return


class ChattyDict(ImmutableDict):

    def __setitem__(self, key, value):
        raise SetAttributeError('Cannot set another value.')

    def __delitem__(self, key):
        raise DeleteAttributeError('Cannot delete key from dictionary.')
