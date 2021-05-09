class Student(object):
    __licznik = 0
    def __init__(self, imie, nazwisko, nr_indeksu, kierunek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.__nr_indeksu = nr_indeksu
        self.kierunek = kierunek
        Student.__licznik = Student.__licznik+1

    def __str__(self):
        return f'Student(imie={self.imie}, nazwisko={self.nazwisko}, nr_indeksu={self.__nr_indeksu}, kierunek={self.kierunek})'

    def compare(self, nazwisko):
        if self.nazwisko < nazwisko:
            return True
        elif self.nazwisko == nazwisko:
            return False
        else:
            return False

    def getLicznik(self):
        return self.__licznik

    def getIndex(self):
        return self.__nr_indeksu




class StudentInformatyki(Student):
    def __init__(self, imie, nazwisko, nr_indeksu, kierunek, specjalnosc):
        super().__init__(imie, nazwisko, nr_indeksu, kierunek)
        self.kierunek = 'IIS'
        self.specjalnosc = specjalnosc

    def __str__(self):
        return f'StudentInformatyki(imie={self.imie}, nazwisko={self.nazwisko}, nr_indeksu={self.getIndex()}, kierunek={self.kierunek}, specjalnosc={self.specjalnosc})'

def testy():
    s1 = Student('Konrad', 'Błaszkiewicz', 19324, 'Informatyka')
    s2 = Student('Jan', 'Kowalski', 10000, 'Informatyka')
    print("Zad 1)")
    print(s1)
    # print(s1.__nr_indeksu) #AttributeError: 'Student' object has no attribute '__nr_indeksu'
    print("Zad 2)")
    if s1.compare(s2.nazwisko):
        print(s1.nazwisko)
    else:
        print(s2.nazwisko)
    print("Zad 3)")
    s3 = Student('Adam', 'Nowicki', 20000, 'Ekonomia')
    print(f'Licznik= {s3.getLicznik()}')
    print("Zad 4)")
    s4 = StudentInformatyki('Alicja', 'Ślimak', 30000,'Informatyka', 'Grafika kompuerowa')
    print(s4)


    pass

if __name__ == "__main__":
    testy()