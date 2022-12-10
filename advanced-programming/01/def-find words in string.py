def find(str,n):
  words = []
  for word in str.split(" "):
    if (len(word) == n):
      words.append(word)
  print("{} words have length {}:\n".format(len(words), n) + ", ".join(words))

find("my name is amir and i love python", 4)
