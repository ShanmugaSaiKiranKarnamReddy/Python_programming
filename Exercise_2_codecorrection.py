def function1(value):
    return value
def function2(func):
    return func()
def function3():
    return 'from 3'

print(function2(function3))