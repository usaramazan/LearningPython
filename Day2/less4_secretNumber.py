secret_number=9
count=0

while count<3:
    number = int(input('guess a number'))
    count += 1
    if number==9:
      print('you won!')
      break

else:
    print('you lost')
