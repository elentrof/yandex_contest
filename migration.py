# Лайнландия представляет из себя одномерный мир, являющийся прямой, на котором располагаются N городов, последовательно пронумерованных от 0 до N - 1 . 
# Направление в сторону от первого города к нулевому названо западным, а в обратную — восточным.
# Когда в Лайнландии неожиданно начался кризис, все были жители мира стали испытывать глубокое смятение. По всей Лайнландии стали ходить слухи, что на востоке живётся лучше, чем на западе.
# Так и началось Великое Лайнландское переселение. Обитатели мира целыми городами отправились на восток, покинув родные улицы, и двигались до тех пор, 
# пока не приходили в город, в котором средняя цена проживания была меньше, чем в родном.

# Формат ввода
# В первой строке дано одно число N  количество городов в Лайнландии. Во второй строке дано N чисел 
#  средняя цена проживания в городах с нулевого по (N - 1)-ый соответственно.
# Формат вывода
# Для каждого города в порядке с нулевого по (N - 1)-ый выведите номер города, в который переселятся его изначальные жители. 
# Если жители города не остановятся в каком-либо другом городе, отправившись в Восточное Бесконечное Ничто, выведите -1 .

n = int(input())
str1 = input()
str1 = str1.strip()

costs = list(map(int, str1.split(' ')))

new_cities = [None] * n
stack = []


for city_num, cost in enumerate(costs):

  if len(stack) == 0: 
    stack.append([city_num, cost])
  else:
    if cost >= stack[-1][1]: #если стоимость текущего больше, чем последний в стеке - отправляем в стек
      stack.append([city_num, cost])
    else:
      for city in reversed(stack): 
        if city[1] > cost: #достаем номер города из стека
          new_cities[city[0]] =  str(city_num)
          stack.pop()
      stack.append([city_num, cost])

for i in stack:
  new_cities[i[0]] = '-1'

print(' '.join(new_cities))