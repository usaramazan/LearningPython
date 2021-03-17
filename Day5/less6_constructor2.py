class Person():
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f'{self.name} is talking')


person=Person('ali')#constructor icine argument gonderdik
print(person.name)
person.talk()

person2=Person('Cemile')
person2.talk()