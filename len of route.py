# В неориентированном графе требуется найти длину минимального пути между двумя вершинами.

# Формат ввода
# Первым на вход поступает число N – количество вершин в графе (1 ≤ N ≤ 100). 
# Затем записана матрица смежности (0 обозначает отсутствие ребра, 1 – наличие ребра). Далее задаются номера двух вершин – начальной и конечной.

# Формат вывода
# Выведите L – длину кратчайшего пути (количество ребер, которые нужно пройти).

# Если пути нет, нужно вывести -1.
f = open('input.txt', 'r')
N = int(f.readline())

gf = [[]] * N
# читаем матрицу смежности
for i in range(N):
  gf[i] = list(map(int, f.readline().strip().split(' ')))


x, y = map(int, f.readline().strip().split())
x, y = x-1, y-1
if x == y:
    print(0)
else:
  # посещенные вершины
  visited = set()
  visited.add(x)
  queue = []
  queue.append((x, [x]))
  flag = 0
  while queue:
    tmp, way = queue.pop()
    if tmp == y:
      flag = 1
      print(len(way) - 1)
      break
    for i in range(N):
      # если есть ребро и вершина не посещена
      if gf[tmp][i] == 1 and i not in visited:
        visited.add(i)
        queue.insert(0, (i, way + [i]))
  if flag == 0:
    print(-1)