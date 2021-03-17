numbers = [5,2,5,2,2]
for item in numbers:
    print('F'* item)
print()

print('=========================')

print()
# other way in below
for x_count in numbers:
    output =""
    for count in range(x_count):
        output+='X'
    print(output)

print('=========================')

sayi=[1,1,1,1,5]
for itm in sayi:
    print('X'*itm)