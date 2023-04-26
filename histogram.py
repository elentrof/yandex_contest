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