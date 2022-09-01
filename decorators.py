


def add_border(func):
    def inner(*args, **kwargs):
        print('-' * 10)
        print()
        result = func(*args, **kwargs)
        print()
        print('-' * 10)
        return result
    return inner

