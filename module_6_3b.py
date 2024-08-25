class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound1 = 'Frrr'


    def run(self, dx):
        self.x_distance += dx
        return self.x_distance

class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound2 = 'I train, eat, sleep, and repeat'


    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance

class Pegasus(Horse, Eagle):

    def __init__(self):
        Eagle.__init__(self)
        Horse.__init__(self)


    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        spr = '!...'
        sound = self.sound1+spr+self.sound2+spr+self.sound1+spr
        print(sound)


p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()
print(Pegasus.mro())