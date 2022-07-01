# Задача 14 Напишите функцию xor(x, y) реализующую функцию "Исключающее ИЛИ" двух логических переменных x и y. Функция xor должна возвращать True, если ровно один из ее аргументов x или y, но не оба одновременно равны True.
def xor(a, b):
    if a == 1 and b == 1:
        return 0
    elif a == 1 or b == 1:
        return 1
    else:
        return 0

x = int(input())
y = int(input())
print(xor(x, y))