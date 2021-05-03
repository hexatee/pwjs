import mojeklasy as mk

def testy():
    p1 = mk.punkt2D(2,5)
    p2 = mk.punkt2D(5,2)
    print('p1')
    p1.drukuj()
    print('\np2')
    p2.drukuj()
    print('\nodcinek')
    odc = mk.odcinek(p1,p2)
    print('długość odcinka: %f' % odc.dlugoscOdc())
    print('\np3d')
    p3d = mk.punkt3D(2,5,2)
    p3d.drukuj()
    pass


if __name__ == "__main__":
    testy()
