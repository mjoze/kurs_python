"""Utwórz dekorator @timepassed mierzący czas działania dowolnej funkcji."""
import time


def timepassed(some_time):
    def nested():
        t1 = some_time()
        t2 = time.time()
        return t2 - t1
    return nested


@timepassed
def now_time():
    return time.time()


a = now_time()
print(a)
