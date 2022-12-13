# Alireza Mohammadi-A
# Sun. 10:10 ~ 12:25

def reverse1(str):
  print(str[::-1])


def reverse2(str):
  reversed = ''
  for i in range(len(str), 0, -1):
    reversed += str[i-1]
  print(reversed)


def reverse3(str):
  reversed = ''
  i = len(str)
  while (i > 0):
    reversed += str[i-1]
    i -= 1
  print(reversed)


reverse1('amir')
reverse2('amir')
reverse3('amir')