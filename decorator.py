import time


def benchmark():
    import time
    def wrapper(*args, **kwargs):
        total = 0
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        total = total + (end - start)
        print('Время выполнения: {} секунд.'.format(total / iters))
        return return_value

    return wrapper


def benchmark(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print('Время выполнения: {} секунд.'.format(total / iters))
            return return_value

        return wrapper

    return actual_decorator


class Benchmark:
    def __init__(self, iters=5):
        self.iters = iters

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print('Время выполнения: {} секунд.'.format(total / iters))
            return return_value

        return wrapper


from functools import wraps


def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)

    return wrapper


@my_decorator
def example():
    """Docstring"""
    print('Called example function')


example()
# >>> example.__name__
# 'example'
# >>> example.__doc__
# 'Docstring'




