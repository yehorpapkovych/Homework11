def outside_func():
    def inside_func():
        return 'hi'
    return inside_func

a = outside_func()
print(a())