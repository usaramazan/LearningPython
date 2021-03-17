numbers = [2,4,3,6,4,8,]
numbers.append(12)# append ile listeye 1 sayisini sona ekledik
#ya ortaya bi yere eklemek istersek napcaz?
print(numbers)

numbers.insert(3,24)#burda 3.index icin 24 olsun istiyoruz
numbers.remove(2)#2.indexi silmek istiyoruz
print(numbers)
#eger listedeki son item i silmek istersek
numbers.pop()
print(numbers)
#eger belli bi indexdeki elemani call etmek istersek
print(numbers.index(3))

names =['ali','veli','hasan']
names.clear()# butun list silinir
print(names)

#aradigimiz deger listemizde var mi yok mu, nasil bakariz
print("aksit" in names)#aksit listede olmadigi icin false
print(4 in numbers)# 4 listede oldugu icin true

# peki aradimiz eleman listemizde kactane var, onu bulmak icin napmali?
print(numbers.count(4))#listemizde 2 tane 4 oldugunu yazdirir

#eger listemizi sort etmek istersek
numbers.sort()#BURDA SOR EDIP ASAGIDA YAZDIRMAK GEREK
print(numbers) # seklinde sort edebilirz, asagisi onemli

print(numbers.sort())# SEKLINDE OLMAZ, BU BI SEY RETURN ETMEZ-NONE OLUR
numbers.reverse()# eger descending order yapmak istersek, once sort et, sonra rever kullan
print(numbers)

numbers2=numbers.copy()# boylece original listin kopyasini olusturduk
numbers.append(56)# original list e 56 ekledik
print(numbers2) # ikinci list yazdirmak istedigimizde original e ekelenen 56 burda yok