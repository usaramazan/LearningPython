name=input('What is your name?')

if len(name)<=3:
    print("name must be at least 4 character")
elif len(name)>15:
    print('name shouldnt be more than 15 character')
else:
    print('name looks good')