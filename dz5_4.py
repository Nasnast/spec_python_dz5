"""Задача 4. Генератор подстрок
Напишите генераторную функцию substrings(s), которая принимает строку
s и возвращает генератор всех возможных подстрок этой строки.
На вход подается строка abc
На выходе будут выведены обозначения:
a
ab
abc
b
bc
c"""


def substrings(s: str) -> (iter, str):
    length = len(s)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield s[start:end]


str = "abcd"
print(*substrings(str))
