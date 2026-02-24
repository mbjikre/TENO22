def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('**********')
        func(*args, **kwargs)
        print('**********')
    return wrap_func

@my_decorator
def hello(a, b=':)'):
    print(a, b)

@my_decorator
def bye():
    print('byyeee!!!!')

hello('print')
bye()