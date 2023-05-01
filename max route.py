# В левом верхнем углу прямоугольной таблицы размером N×M
# находится черепашка. В каждой клетке таблицы записано некоторое число. Черепашка может перемещаться вправо или вниз, при этом маршрут черепашки заканчивается в правом нижнем углу таблицы.
# Подсчитаем сумму чисел, записанных в клетках, через которую проползла черепашка (включая начальную и конечную клетку). 
# Найдите наибольшее возможное значение этой суммы и маршрут, на котором достигается эта сумма.

# Формат ввода
# В первой строке входных данных записаны два натуральных числа N и M, не превосходящих 100 — размеры таблицы. 
# Далее идет N строк, каждая из которых содержит M чисел, разделенных пробелами — описание таблицы. 
# Все числа в клетках таблицы целые и могут принимать значения от 0 до 100.
# Формат вывода
# Первая строка выходных данных содержит максимальную возможную сумму, вторая — маршрут, на котором достигается эта сумма. 
# Маршрут выводится в виде последовательности, которая должна содержать N-1 букву D, означающую передвижение вниз и M-1 букву R, означающую передвижение направо. 
# Если таких последовательностей несколько, необходимо вывести ровно одну (любую) из них.

f = open('input.txt', 'r')
N, M = map(int, f.readline().strip().split(' '))

dp =[[0]*M for i in range(N)]
mas = [[0]] * N
for i in range(0, N):
  k = list(map(int, f.readline().strip().split(' ')))
  mas[i] = k

dp[0][0] = mas[0][0]

route = ''
# база дп - первая строка и первый столбец
for j in range(1, M):
  dp[0][j]=dp[0][j-1]+mas[0][j]
for i in range(1,N):
  dp[i][0]=dp[i-1][0]+mas[i][0]

for i in range(1, N):
  for j in range(1,M):
    dp[i][j]=max(dp[i][j-1], dp[i-1][j])+mas[i][j]

# восстановление пути 
r, d = N-1, M-1
while r > 0 or d > 0:
  if dp[r-1][d] > dp[r][d-1]:
    if r > 0:
      r -= 1
      route = 'D' + route 
    else: 
      d -= 1
      route = 'R' + route 
  else:
    if d > 0:
      d -= 1
      route = 'R' + route 
    else: 
      r -= 1
      route = 'D' + route 
    
  

print(dp[-1][-1])
print(route)