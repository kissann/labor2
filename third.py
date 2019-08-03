import math
#Задача 3.
#Знайти найбільшу висоту трикутника, який задано довжинами його сторін.
#Обов'язкове перевірка існування трикутника.

print("Введите длину сторон треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a+b>c and a+c>b and b+c>a :
    p=(a+b+c)/2
    print("Полупериметр p=%.2f:"%p)
    ha=(2/a)*math.sqrt(p*(p-a)*(p-b)*(p-c))
    hb=(2/b)*math.sqrt(p*(p-a)*(p-b)*(p-c))
    hc=(2/c)*math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Высоты треугольника ha=%.2f,hb=%.2f,hc=%.2f:"%(ha,hb,hc))
    maxH=max(ha,hb,hc)
    print("Наибольшая высота H=%.2f:"% maxH)
else:
    print("Не существует треугольника")