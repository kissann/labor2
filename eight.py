#Задача 8.
#Вивести всі парні цілі числа від 1 до числа m.
print("Введите число:")
a = int(input("Число = "))
for i in range(1,a):
    if i%2==0:
        print(i)
