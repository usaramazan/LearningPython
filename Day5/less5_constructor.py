class Point():
    def greeting(self):
        print('hi how are you?')

    def __init__(self,x,y):#constructor burda define ettik
        self.x = x
        self.y = y

point = Point(12,34)# constructor i obj olustururken direkt kullandik
print(point.x)
