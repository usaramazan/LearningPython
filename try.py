import try2# bu sekilde butun file i import etmis olduk ama istersek
# file icindeki specific function da import edebiliriz


result=try2.lbs_to_kg(24)
print(result)

#note: eger python un kendisinde olan bi key word kullanirsan
# o kelimenin altinda sari bi dalga isareti cikar ve ustune gidersen
# 'shadow built-in name' seklinde bi uyari verir.

import Day6_ecommerce.shipping # boylece shipping module import edildi

#simdi de icindeki function kulanalim
Day6_ecommerce.shipping.calc_shipping()

#Diger bi import yontemi de: butun module import etmek yerine istedigimiz function i import edebilirz
from Day6_ecommerce.shipping import calc_shipping #Day6_ecommerce icindeki shipping module import et
# istersek Day6_ecommerce tamamen de import edebiliirz
calc_shipping()

import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(4,9)) #4 ile 9 arasindan rastgele sayi sececek.

members = ['ali','veli','ayhan','orhan']
leader = random.choice(members)
print(leader)

#lets role 2 dice
def roll():
    first = random.randint(1,6)
    second = random.randint(1,6)
    return (first,second)

print(roll())