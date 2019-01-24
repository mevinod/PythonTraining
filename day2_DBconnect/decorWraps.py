def add_num_decorate(fun):
    def wrap_add_num(a, b):
        print('Before adding')
        a = a + 1
        print('before ops', a)
        print(fun(a, b))
        print('After adding')
        b = b - 1
        print("TestAfter", b)
    return wrap_add_num


@add_num_decorate
def add_num(a, b):
    return a + b


a = input("Enter First number: ")
b = input("Enter second number: ")
a = int(a)
b = int(b)
add_num(a, b)
