def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operator(func, x):
    result = func(x)
    return result


num = input("Enter a number: ")
num = int(num)

print(operator(inc, num))
print(operator(dec, num))
