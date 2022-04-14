from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs == {}:
            res = func(*args)
            msg = ''
            for el in range(len(args)):
                if el == 0:
                    msg += f'{args[el]}: {type(args[el])}'
                else:
                    msg += f', {args[el]}: {type(args[el])}'
        else:
            res = func(*args, **kwargs)
            msg = ''
            el = 0
            for val in kwargs.values():
                if el == 0:
                    msg += f'{val}: {type(val)}'
                    el += 1
                else:
                    msg += f', {val}: {type(val)}'
        print(msg)
        print(f'{func.__name__}({msg})')
        return res

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def calc_x_y(x, y):
    return x * y


print(calc_cube(x=3))
print(calc_cube(7.2))
print(calc_x_y(5, 6.5))
print(calc_x_y(x=5, y=6))
