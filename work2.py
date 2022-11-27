# Задайте список из n чисел последовательности (1 + 1/n)^n. 
# Вывестив консоль сам список и сумму его элементов.


numbers = int (input ('Введите количество чисел в списке '))
summ = 0
list = []

for i in range(1, numbers + 1) :
     list.append (round ((1 + 1 / i) ** i, 3))
     summ += list[i - 1]

print (f'Последовательность: {list}') 
print (f'Сумма: {round (summ, 3)}')