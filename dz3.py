def greet(name):
    return print("Привет",name)
greet('Саша')

def square(number):
    return print(number**2)
square(10)

def max_of_two(x,y):
    if x > y:
        return print(x)
    else:
        return print(y)
max_of_two(24,54)


def describe_person(name,age=30):
    return print(name,age,'лет')
describe_person('Миша')


def is_prime(number):
    d = 2
    while number % d != 0:
        d += 1
    return print(d == number)
is_prime(8)