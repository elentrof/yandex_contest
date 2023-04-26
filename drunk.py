# В игре в пьяницу карточная колода раздается поровну двум игрокам. Далее они вскрывают по одной верхней карте, и тот, чья карта старше, забирает себе обе вскрытые карты, 
# которые кладутся под низ его колоды. Тот, кто остается без карт – проигрывает. Для простоты будем считать, что все карты различны по номиналу, а также, 
# что самая младшая карта побеждает самую старшую карту ("шестерка берет туза"). Игрок, который забирает себе карты, сначала кладет под низ своей колоды карту первого игрока, 
# затем карту второго игрока (то есть карта второго игрока оказывается внизу колоды). Напишите программу, которая моделирует игру в пьяницу и определяет, кто выигрывает. 
# В игре участвует 10 карт, имеющих значения от 0 до 9, большая карта побеждает меньшую, карта со значением 0 побеждает карту 9.

# Формат ввода
# Программа получает на вход две строки: первая строка содержит 5 чисел, разделенных пробелами — номера карт первого игрока, 
# вторая – аналогично 5 карт второго игрока. Карты перечислены сверху вниз, то есть каждая строка начинается с той карты, которая будет открыта первой.

# Формат вывода
# Программа должна определить, кто выигрывает при данной раздаче, и вывести слово first или second, после чего вывести количество ходов, 
# сделанных до выигрыша. Если на протяжении 106 ходов игра не заканчивается, программа должна вывести слово botva.

str1 = input()
str2 = input()

player1 = str1.strip().split(' ')
player2 = str2.strip().split(' ')

n = 0
max_ = 1000000
# пока не закончатся карты у игрока или количество ходов станет 10^6
while len(player1) != 0 and len(player2) != 0 and n <= max_: 
  card1 = player1.pop(0)
  card2 = player2.pop(0)
  
  # случай сравнения 0 и 9 отдельный
  if card1 == '0' and card2 == '9':
    player1.append(card1)
    player1.append(card2)
  elif card2 == '0' and card1 == '9':
    player2.append(card1)
    player2.append(card2)
  elif card1 > card2:
    player1.append(card1)
    player1.append(card2)
  else:
    player2.append(card1)
    player2.append(card2)
  n += 1

if n == max_:
  print('botva')
elif len(player1) > 0:
  print(f'first {n}')
else:
  print(f'second {n}')