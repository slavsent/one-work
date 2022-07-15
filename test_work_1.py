def task(array):
    return array.index('0')


print(task("111111111110000000000000000"))


def task1(array):
    for i in range(len(array)):
        if array[i] == '0':
            return i


print(task1("111111111110000000000000000"))
