# Вовочка ломает систему безопасности Пентагона. Для этого ему понадобилось узнать, какие символы в секретных зашифрованных посланиях употребляются чаще других. 
# Для удобства изучения Вовочка хочет получить графическое представление встречаемости символов. Поэтому он хочет построить гистограмму количества символов в сообщении. 
# Гистограмма — это график, в котором каждому символу, встречающемуся в сообщении хотя бы один раз, соответствует столбик, высота которого пропорциональна количеству этих символов в сообщении.

# Формат ввода
# Входной файл содержит зашифрованный текст сообщения. Он содержит строчные и прописные латинские буквы, цифры, знаки препинания («.», «!», «?», «:», «-», «,», «;», «(», «)»), пробелы и переводы строк.
# Размер входного файла не превышает 10000 байт. Текст содержит хотя бы один непробельный символ. Все строки входного файла не длиннее 200 символов.
# Для каждого символа c кроме пробелов и переводов строк выведите столбик из символов «#», количество которых должно быть равно количеству символов c в данном тексте.
# Под каждым столбиком напишите символ, соответствующий ему. Отформатируйте гистограмму так, чтобы нижние концы столбиков были на одной строке, первая строка и первый столбец были непустыми.
# Не отделяйте столбики друг от друга. Отсортируйте столбики в порядке увеличения кодов символов.

f = open('input.txt', 'r')
msg = ''
for line in f:
  line = line.strip()
  msg += line

letters_dict = {}

for letter in msg:
  # letters_dict[letter] = letters_dict.get(letter, 0) + 1
  if letter != ' ':
    if letter in letters_dict.keys():
      letters_dict[letter] += 1
    else:
      letters_dict[letter] = 1

sorted_letters = sorted(letters_dict.items(), key=lambda x: x[0])
max_ = max(letters_dict.values())

n = len(sorted_letters)
mas = [' '] * (max_+1)
for i in range(max_+1): 
  mas[i] = [' '] * (n+1)

for i in range(max_, 0, -1):
  for j, let in enumerate(sorted_letters):
    if let[1] >= i:
      mas[max_-i][j] = '#'

for j, l in enumerate(sorted_letters):
  mas[-1][j] = l[0]


for i in mas: 
    for i2 in i: 
        print(i2, end='') 
    print()