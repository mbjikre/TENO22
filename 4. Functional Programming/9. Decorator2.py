from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} ms to complete')
        return result
    return wrapper

@performance
def long_time():
    for i in range(999999999):
        i*5

long_time()