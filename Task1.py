def test():
    a = 5
    b = 9
    c = 'llll'
    d = 'pppp'

def func(func1):
    code = func1.__code__
    return code.co_nlocals

print(func(test))