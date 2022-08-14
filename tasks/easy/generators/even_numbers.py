"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


def get_even_number():
    n = 1
    while True:
        yield n + 1
        n += 2


even_gen = get_even_number()


print(next(even_gen))
print(next(even_gen))
print(next(even_gen))
print(next(even_gen))
