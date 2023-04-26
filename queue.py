# Научитесь пользоваться стандартной структурой данных queue для целых чисел. Напишите программу, содержащую описание очереди и моделирующую работу очереди, реализовав все указанные здесь методы. 

# Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После выполнения каждой команды программа должна вывести одну строчку.

# Возможные команды для программы:

# push n
# Добавить в очередь число n (значение n задается после команды). Программа должна вывести ok.

# pop
# Удалить из очереди первый элемент. Программа должна вывести его значение.

# front
# Программа должна вывести значение первого элемента, не удаляя его из очереди.

# size
# Программа должна вывести количество элементов в очереди.

# clear
# Программа должна очистить очередь и вывести ok.

# exit
# Программа должна вывести bye и завершить работу.

# Перед исполнением операций front и pop программа должна проверять, содержится ли в очереди хотя бы один элемент. Если во входных данных встречается операция front или pop, и при этом очередь пуста, то программа должна вместо числового значения вывести строку error.

# Формат ввода
# Вводятся команды управления очередью, по одной на строке

# Формат вывода
# Требуется вывести протокол работы очереди, по одному сообщению на строке

f = open('input.txt', 'r')

mas = []
for line in f:
  line = line.strip()
  if len(line.split(' ')) == 2:
    str = line.split(' ')
    mas.append(int(str[1]))
    print('ok')
  elif line == 'pop':
    if len(mas) >= 1:
      print(mas[0])
      mas.pop(0)
    else:
      print('error')
  elif line == 'front':
    if len(mas) >= 1:
      print(mas[0])
    else:
      print('error')
  elif line == 'size':
    print(len(mas))
  elif line == 'clear':
    mas = []
    print('ok')
  else:
    print("bye")
    break