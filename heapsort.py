# Отсортируйте данный массив. Используйте пирамидальную сортировку.

# Формат ввода
# Первая строка входных данных содержит количество элементов в массиве N, N ≤ 105. Далее задаются N целых чисел, не превосходящих по абсолютной величине 109.

# Формат вывода
# Выведите эти числа в порядке неубывания.

n = int(input())
str1 = input()

heap_list = list(map(int, str1.strip().split(' ')))

def max_heapify(heap_list, i, heap_size):
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

def build_max_heap(heap_list, heap_size):  
  for i in range(int(len(heap_list)/2)-1, -1, -1):
    heap_list = max_heapify(heap_list, i, heap_size)
  return heap_list

def heapsort(heap_list):
  """
  пирамидальная сортировка
  """
  heap_size = len(heap_list)
  heap_list = build_max_heap(heap_list, heap_size)
  for i in range(len(heap_list)-1, 0, -1):
    heap_list[0], heap_list[i] = heap_list[i], heap_list[0]
    heap_size -= 1
    heap_list = max_heapify(heap_list, 0, heap_size)
  return heap_list


heap_list = heapsort(heap_list)  
print(' '.join(str(x) for x in heap_list))