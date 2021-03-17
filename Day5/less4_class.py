class Point:   #in pascal name in convention, we use capital letter for first letter in class name
    def move(self):
        print("move")

    def draw(self):
        print('draw')


#lets create obj for Point class
point1=Point()
point1.draw() #class icindeki draw function call ettik
point1.move()
point1.x=10
point1.y=34
print(point1.x)