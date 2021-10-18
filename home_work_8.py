#1

from functools import wraps
import re
EMAIL = re.compile(r'([a-z0-9_\.]+)@([a-z0-9]+\.[a-z]+)')
def email_parse(email):
    found_info = EMAIL.findall(email)[0]
    if found_info:
        name, addr = found_info
    else:
        raise ValueError(f'wrong email: {email}')
    print(name, addr)

#3
def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)

    return wrapper


@type_logger
def calc_cube(*args):
    return list(map(lambda x: x ** 3, args))


a = calc_cube(5, 3)


#4

def val_checker(decorator_check_func):
    def _val_checker(func_calc_cube):
        @wraps(func_calc_cube)  # нужно указать от какой функции
        def wrapped(x):
            if decorator_check_func(x):
                return func_calc_cube(x)
            else:
                raise ValueError(x)

        return wrapped
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    """calc_cube desc"""
    return x ** 3


a = calc_cube(5)