def f(x):
    x += 10
    print(x)
    raise Exception('inside f')


def g(y):
    y += 100
    f(y)


a = 10

g(a)
