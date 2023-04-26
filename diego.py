# Диего увлекается коллекционированием наклеек. На каждой из них написано число, и каждый коллекционер мечтает собрать наклейки со всеми встречающимися числами.

# Диего собрал N наклеек, некоторые из которых, возможно, совпадают. Как-то раз к нему пришли K коллекционеров. 
# i-й из них собрал все наклейки с номерами не меньшими, чем pi. Напишите программу, которая поможет каждому из коллекционеров определить, сколько недостающих ему наклеек есть у Диего. 
# Разумеется, гостей Диего не интересуют повторные экземпляры наклеек.

# Формат ввода
# В первой строке содержится единственное число N (0 ≤ N ≤ 100 000) — количество наклеек у Диего.

# В следующей строке содержатся N целых неотрицательных чисел (не обязательно различных) — номера наклеек Диего. Все номера наклеек не превосходят 109.

# В следующей строке содержится число K (0 ≤ K ≤ 100 000) — количество коллекционеров, пришедших к Диего. 
# В следующей строке содержатся K целых чисел pi (0 ≤ pi ≤ 109), где pi — наименьший номер наклейки, не интересующий i-го коллекционера.

# Формат вывода
# Для каждого коллекционера в отдельной строке выведите количество различных чисел на наклейках, которые есть у Диего, но нет у этого коллекционера.

f = open('input.txt', 'r')
n = int(f.readline().strip())
sticker_number = f.readline().strip()
k = int(f.readline().strip())
p = f.readline().strip()

def binary_search(data, elem):
    low = 0
    high = len(data) - 1

    while low <= high:      
        middle = (low + high)//2
       
        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1   

    return middle

if n != 0 and k != 0:
  diego_mass = []
  for i in sticker_number.strip().split(' '):
    diego_mass.append(int(i))
  # сортируем карточки диего
  dm = sorted(set(diego_mass))

  # наклейки коллекционеров
  mas = list(map(int, p.split(' ')))
  # бинарным поиском ищем количество различных чисел на наклейках, которые есть у Диего, но нет у этого коллекционера.
  for col in mas:
    mid = binary_search(dm, col)

    if col > dm[mid]:
      mid += 1
    
    print(mid)

elif k != 0:
  for i in range(k):
    print(0)
else:
  print(0)