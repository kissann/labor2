#Задача 6.
#Складіть програму, яка за введеним номером кольора у веселці (1-7) виводить на екран назву відповідного кольору
#(1 червоний, 2 помаранчевий, ...). Якщо введено будь-яке інше число, то програма повинна виводити повідомлення про помилку.
print("Введите номер цвета радуги:")
a = int(input("Номер цвета = "))
color = ["красный","оранжевый", "жёлтый", "зелёный","голубой","синий","фиолетовый"]
if a<7:
    print(color[a])
else:
    print("Нет такого цвета в радуге")
