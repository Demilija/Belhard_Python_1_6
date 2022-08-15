"""
Написать рекурсивную функцию fibonacci, которая будет возвращать n-ый элемент
"""


def fibonacci(n: int):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
