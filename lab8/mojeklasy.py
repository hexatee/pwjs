import math

class punkt2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drukuj(self):
        print('x= %d' % self.x)
        print('y= %d ' % self.y)

    def zeruj(self):
        self.x = 0
        self.y = 0

class punkt3D(punkt2D):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def drukuj(self):
        print('x= %d' % self.x)
        print('y= %d ' % self.y)
        print('z= %d' % self.z)

    def zeruj(self):
        self.x = 0
        self.y = 0
        self.z = 0

class odcinek():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def dlugoscOdc(self):
        x = (self.p2.x - self.p1.x)**2
        y = (self.p2.y - self.p1.y)**2
        return math.sqrt(x+y)



def testy():
    print('punkt2D:')
    p1 = punkt2D(5, 10)
    p1.drukuj()
    p1.zeruj()
    p1.drukuj()
    print('\npunkt3D:')
    p2 = punkt3D(9,12,3)
    p2.drukuj()
    p2.zeruj()
    p2.drukuj()
    print('\nodcinek')
    p3 = punkt2D(10,5)
    odc = odcinek(p1,p3)
    print('Długość odcinka: %f' % odc.dlugoscOdc())
    pass

if __name__ == "__main__":
    testy()