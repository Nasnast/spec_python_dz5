"""Задача 3. Генератор последовательности чисел Фибоначчи
Напишите генераторную функцию fibonacci(n), которая принимает на вход
одно целое число n и возвращает последовательность первых n чисел
Фибоначчи. Числа Фибоначчи — это последовательность, в которой каждое
число является суммой двух предыдущих, начиная с 0 и 1."""


# 1
def fibonacci(n: int) -> (iter, int):
    fibo_list = [0, 1, 1]
    current_number = 0
    while current_number < n:
        while len(fibo_list) < n:
            fibo_list.append(sum(fibo_list[-2:]))
        yield fibo_list[current_number]
        current_number += 1


print(*fibonacci(7))


# 2
def fibonacci_2(n: int) -> (iter, int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(*fibonacci_2(12))
