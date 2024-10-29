"""Задача 2. Однострочный генератор словаря
Напишите однострочный генератор словаря, который принимает на вход три
списка одинаковой длины: имена str, ставка int, премия str с указанием
процентов вида 10.25%.
В результате result получаем словарь с именем в качестве ключа и суммой
премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии.
Не забудьте распечатать в конце результат.
Пример использования.
На входе:
names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]
На выходе:
{'Alice': 500.0, 'Bob': 300.0, 'Charlie': 1050.0}"""


# 1
def premium(names: list[str], salary: list[int], bonus: list[str]) -> dict[str:float]:
    return {
        names[i]: salary[i] * float(bonus[i].strip("%")) / 100
        for i in range(len(names))
    }


names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]
print(premium(names, salary, bonus))

# 2
new_dict = {}
for names, salary, bonus in zip(names, salary, bonus):
    new_dict[names] = salary * float(bonus[:-1]) / 100
print(new_dict)
