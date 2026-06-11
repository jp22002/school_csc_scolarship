def find_missing():
  dicti = {}
  run = 0
  while run < 7:
    run += 1
    sock_color = input('What color sock? ')
    if sock_color in dicti.keys():
      dicti[sock_color] += 1
    else:
      dicti[sock_color] = 1
  run = 0
  for i in dicti:
    if (dicti[i]) % 2 != 0:
      print(f"Emma! Where is your {i} sock?")
    run += 1

  
find_missing()
