names=['ali','veli','ak','karan','selim']
print(names)
print(names[3])
print(names[1:4])#birnci index dahil ama 4.index dahil degil
print(names[2:])#2. indexden baslar sona kadar gider
print(names[-1])# son indexdekini yazdirir.
# diyelim ki listede 1.siradaki ismi degistirmek istiyoruz
names[0]='Can'
names.append('cem') #sona 'cem' ekler
print(names)