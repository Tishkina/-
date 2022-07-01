# Задача 13 В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
a = [int(i) for i in input().split()]
b = 0
c = 0
for i in a:
    b = a.index(min(a))
    c = a.index(max(a))
a[c], a[b] = a[b], a[c]
print(' '.join([str(i) for i in a]))