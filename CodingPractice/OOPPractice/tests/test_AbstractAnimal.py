import unittest

from CodingPractice.OOPPractice.assignments.AbstractAnimal import *


class TestAbstractAnimal(unittest.TestCase):

    def test_01_can_construct_horse(self):
        a = Horse('brown', 'female', 'dolly')

        self.assertEqual('brown', a.get_colour())
        self.assertEqual('female', a.get_sex())
        self.assertEqual('dolly', a.get_name())

        self.assertEqual(1, a.get_instance_count())

    def test_02_horse_walk(self):
        a = Horse('brown', 'female', 'dolly')

        self.assertEqual('I am a horse walking!', a.walk())

    def test_03_can_construct_bird_with_flight(self):
        a = BirdWithFlight('s', 'green', 'male', 'eric')

        self.assertEqual('s', a.get_feather_length())
        self.assertEqual('green', a.get_colour())
        self.assertEqual('male', a.get_sex())
        self.assertEqual('eric', a.get_name())

        self.assertEqual(3, a.get_instance_count())

    def test_04_bird_with_flight_can_fly(self):
        a = BirdWithFlight('s', 'green', 'male', 'eric')

        self.assertEqual('I am flying.', a.fly())

    def test_05_can_construct_pegasus(self):
        a = Pegasus('l', 'white', 'male', 'Pegasus')

        self.assertEqual('l', a.get_feather_length())
        self.assertEqual('white', a.get_colour())
        self.assertEqual('male', a.get_sex())
        self.assertEqual('Pegasus', a.get_name())

        self.assertEqual(5, a.get_instance_count())

    def test_06_pegasus_can_walk(self):
        a = Pegasus('l', 'white', 'male', 'Pegasus')

        self.assertEqual('I am a horse walking!', a.walk())

    def test_07_can_construct_ostrich(self):
        a = Ostrich('l', 'brown', 'female', 'adriana')

        self.assertEqual('l', a.get_feather_length())
        self.assertEqual('brown', a.get_colour())
        self.assertEqual('female', a.get_sex())
        self.assertEqual('adriana', a.get_name())

        self.assertEqual(7, a.get_instance_count())

    def test_08_ostrich_can_walk(self):
        a = Ostrich('l', 'brown', 'female', 'adriana')

        self.assertEqual('I am an ostrich walking!', a.walk())

    def test_09_can_construct_penguin(self):
        a = Penguin('s', 'black', 'female', 'jerry')

        self.assertEqual('s', a.get_feather_length())
        self.assertEqual('black', a.get_colour())
        self.assertEqual('female', a.get_sex())
        self.assertEqual('jerry', a.get_name())

        self.assertEqual(9, a.get_instance_count())

    def test_10_penguin_can_swim_and_walk(self):
        a = Penguin('s', 'black', 'female', 'jerry')

        self.assertEqual('I am swimming.', a.swim())
        self.assertEqual('I am a penguin walking!', a.walk())


if __name__ == '__main__':
    unittest.main()
