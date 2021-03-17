class Animal:
    def walk(self):
        print('walking')


class Dog(Animal):
  pass #pytonda bi class ici bos olamaz, hata verir
        #bunu engellemek icin 'pass' kullanabiliriz
        # ama istesek icine baska methodlar yazabilirdik.


class Cat(Animal):
    pass


dog1 = Dog()
dog1.walk()
cat1 = Animal()#burda Cat() koyabiliyorduk, ama javadaki gibi polymorphism olurmu diye denedim oldu.
cat1.walk()
