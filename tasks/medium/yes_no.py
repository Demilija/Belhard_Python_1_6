"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(lst: int):
    for num, element in enumerate(lst):
        if element in lst[:num]:
            print('Yes')
        else:
            print('No')
