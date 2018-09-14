from abc import ABC, abstractmethod


class Animal(ABC):
    _instance_count = 0

    def __init__(self, colour, sex, name):
        self._colour = colour
        self._sex = sex
        self._name = name
        Animal.incr_instance_count()

    @classmethod
    def incr_instance_count(cls):
        cls._instance_count += 1

    @abstractmethod
    def walk(self):
        return

    def get_colour(self):
        return self._colour

    def get_sex(self):
        return self._sex

    def get_name(self):
        return self._name

    @classmethod
    def get_instance_count(cls):
        return cls._instance_count


class Horse(Animal):

    def walk(self):
        return 'I am a horse walking!'


class Avian(Animal):

    def __init__(self, feather_length, colour, sex, name):
        self._feather_length = feather_length
        Animal.__init__(self, colour, sex, name)

    def get_feather_length(self):
        return self._feather_length


class CanFly:

    def fly(self):
        return 'I am flying.'


class BirdWithFlight(CanFly, Avian):

    def walk(self):
        return 'I am a bird walking!'


class Pegasus(Horse, BirdWithFlight):
    pass


class Ostrich(Avian):

    def walk(self):
        return 'I am an ostrich walking!'


class CanSwim:

    def swim(self):
        return 'I am swimming.'


class Penguin(Avian, CanSwim):

    def walk(self):
        return 'I am a penguin walking!'
