# На клетчатой плоскости закрашено K клеток. Требуется найти минимальный по площади прямоугольник, со сторонами, параллельными линиям сетки, покрывающий все закрашенные клетки.

# Формат ввода
# Во входном файле, на первой строке, находится число K (1 ≤ K ≤ 100). На следующих K строках находятся пары чисел Xi и Yi – координаты закрашенных клеток (|Xi|, |Yi| ≤ 109).

# Формат вывода
# Выведите в выходной файл координаты левого нижнего и правого верхнего углов прямоугольника.

k = int(input())
# массив х
mas1 = [None] * k
# массив y
mas2 = [None] * k
for i in range(k):
  str = input()
  mas1[i], mas2[i] = map(int, str.split(' '))

# прямоугольник покрывает поверхность от минимальной координаты по x, минимальной по y 
# до максимальной по x и максимальной по y
x1 = min(mas1)
y1 = min(mas2)
x2 = max(mas1)
y2 = max(mas2)

print(f'{x1} {y1} {x2} {y2}')