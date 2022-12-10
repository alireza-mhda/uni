def reverse1(str):
  print(str[::-1])

reverse1('amir')
  
def reverse2(str):
  reversed = ''
  for i in range(len(str),0,-1):
    reversed += str[i-1]
  print(reversed)
  
reverse2('amir')

def reverse3(str):
  reversed = ''
  i = len(str)
  while(i > 0):
    reversed += str[i-1]
    i-=1
  print(reversed)
  
reverse3('amir')    
