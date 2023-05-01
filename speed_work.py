import functools
import time


def speed_work_dec(func):
    """Подсчет времени выполнения функции"""
    top = True
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal top
        if top:
            top = False
            start_work = time.perf_counter()
            res = func(*args, **kwargs)
            res_time = time.perf_counter() - start_work
            return (f"Время выполнения функции {func.__name__}: {res_time} сек.\nРезультат выполнения функции: {res}\n")
        else:
            res = func(*args, **kwargs)
            return res

    return wrapper


if __name__ == "__main__":
    pass
