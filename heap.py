# В этой задаче вам необходимо самостоятельно (не используя соответствующие классы и функции стандартной библиотеки) организовать структуру данных Heap для хранения целых чисел, 
# над которой определены следующие операции: a) Insert(k) – добавить в Heap число k ; b) Extract достать из Heap наибольшее число (удалив его при этом).

# Формат ввода
# В первой строке содержится количество команд N (1 ≤ N ≤ 100000), далее следуют N команд, каждая в своей строке. Команда может иметь формат: “0 <число>” или “1”, 
# обозначающий, соответственно, операции Insert(<число>) и Extract. Гарантируется, что при выполнении команды Extract в структуре находится по крайней мере один элемент.

# Формат вывода
# Для каждой команды извлечения необходимо отдельной строкой вывести число, полученное при выполнении команды Extract.

f = open('input.txt', 'r')
n = int(f.readline())

def push_heap(heap_list, x):
  """
  добавление элемента в кучу
  """
  heap_list.append(x)
  pos = len(heap_list) - 1
  while pos > 0 and heap_list[pos] > heap_list[(pos-1) // 2]:
    heap_list[pos], heap_list[(pos-1) // 2] = heap_list[(pos-1) // 2], heap_list[pos]
    pos = (pos - 1) // 2

def max_heapify(heap_list, i, heap_size):
  """
  перестроение кучи
  """
  l = 2 * i + 1
  r = 2 * i + 2
  if l < heap_size and heap_list[l] > heap_list[i]:
    max_ind = l
  else:
    max_ind = i
  if r < heap_size and heap_list[r] > heap_list[max_ind]:
    max_ind = r
  if max_ind != i:
    heap_list[i], heap_list[max_ind] = heap_list[max_ind], heap_list[i]
    heap_list = max_heapify(heap_list, max_ind, heap_size) 
  return heap_list

def heap_extract_max(heap_list):
  """
  извлечение максимального элемента кучи
  """
  heap_size = len(heap_list)
  if heap_size < 1:
    print('0')
  else:
    max_ = heap_list[0]
    heap_list[0] = heap_list[-1]
    heap_size -= 1
    heap_list.pop()
    max_heapify(heap_list, 0, heap_size)
  return max_


heap_list = []

for i in range(n):
  cmd = f.readline().strip().split(' ');
  if len(cmd) == 2:
    push_heap(heap_list, int(cmd[1]))
  else:    
    print(heap_extract_max(heap_list)) 