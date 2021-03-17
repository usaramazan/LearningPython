# try-except block kullaniyoruz.
#ornegin kullanicidan yasini sorcaz, eger kullanici
# gecerli bi sey girmezse kodun hata vermesini istemiyorsak
# exception kullanarak gecerli bi veri girilmediginden
# haberdar oluruz.Ayni zamanda kodun hata vermesi engellenir
# ve kodun devami normal calismasi saglanir.
try:
    age=int(input("age: "))
    print(age)
except ValueError:
    print("Invalid value entered")

#bu kullandigimiz block saedce ValueErrorile ilgili ise ise yarar.
#asagidaki ornekdeki gibi age=0 durumunda farkli kullannak lazim.

try:
    age=int(input("age: "))
    income =2000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('age can not be zero')
except ValueError:
    print("Invalid value entered")

#nasil ki java da try catch block icinde birden fazla catch kullanabiliyorduk,
#pythonda da birden fazla except ____ kullanabiliyoruz