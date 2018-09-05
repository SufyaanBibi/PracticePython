class Animal(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('%s is eating  %s' % (self.name, food))


class Dog(Animal):

    def fetch(self, thing):
        print('%s goes after %s' % (self.name, thing))

    def bark(self, person):
        print('%s is barking at %s' % (self.name, person))


class Cat(Animal):

    def swatstring(self):
        print('%s swats the string!' % self.name)

    def chase(self, thing):
        print('%s chases after %s' % (self.name, thing))


class Bird(Animal):

    def fly(self, place):
        print('%s flies %s' % (self.name, place))

    def sing(self):
        print('%s is singing.' % self.name)


b = Bird('Tweety')
c = Cat('Lulu')
d = Dog('Charlie')

b.fly('home.')
d.fetch('ball.')
c.swatstring()

b.eat('flies.')
d.eat('chicken.')
c.eat('cat food.')

b.sing()
c.chase('a mouse.')
d.bark('Sufyaan.')