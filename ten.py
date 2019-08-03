#Задача 10.
#Знайти всі дільники числа N.
import math
print("Введите число:")
a = int(input("Число = "))
for i in range(1,a+1):
    if a%i==0:
        print(i)