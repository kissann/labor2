#Задача 9.
#Задано деяке число N. Вивести всі прості числа менші за N.
print("Введите число:")
a = int(input("Число = "))
for num in range(1,a):
    if all(num%i!=0 for i in range(2,num)):
       print(num)