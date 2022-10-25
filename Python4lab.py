# cozdanie klassov (5 wtuk)
class Avtomobili():
    def __init__(self, nazvanieavto, marka, godproizvodstva, color, kategoriya, price):
        self.nazvanieavto = nazvanieavto
        self.marka = marka
        self.godproizvodstva = godproizvodstva
        self.color = color
        self.kategoriya = kategoriya
        self.price = price
    def info(self):
        print(self.nazvanieavto)
        print(self.marka)
        print(self.godproizvodstva)
        print(self.color)
        print(self.kategoriya)
        print(self.price)











class MarkaAvto():
    def __init__(self, nazvaniemarki, stranaproizvoditel, zavodproizvoditel, adres):
        self.nazvaniemarki = nazvaniemarki
        self.stranaproizvoditel = stranaproizvoditel
        self.zavodproizvoditel = zavodproizvoditel
        self.adres = adres
    def info(self):
        print(self.nazvaniemarki)
        print(self.stranaproizvoditel)
        print(self.zavodproizvoditel)
        print(self.adres)










# cozdanie inkapsulyazii

class Sotrudniki():
    def __init__(self, familiya, imya, ot4estvo, staj, zarplata):
        self.__familiya = familiya
        self.__imya = imya
        self.__ot4estvo = ot4estvo
        self.__staj = staj
        self.__zarplata = zarplata

    def add__staj(self, value):
        self.__staj = value

    def get_staj(self):
        print(self.__staj)

    def info(self):
        print(self.__familiya)
        print(self.__imya)
        print(self.__ot4estvo)
        print(self.__staj)
        print(self.__zarplata)

# cozdanie svoistva

@property
def zarplata(self): 
    return self.__zarplata

counter = Sotrudniki("ivanov", "artem", "malovich", "10", "25000")
counter.get_staj()
counter.info()









class ProdajaAvto():
    def __init__(self, data, sotrudnik, avtomobil, pokupatel):
        self.data = data
        self.sotrunik = sotrudnik
        self.avtomobil = avtomobil
        self.pokupatel = pokupatel
    def info(self):
        print(self.data)
        print(self.sotrunik)
        print(self.avtomobil)
        print(self.pokupatel)





 





class Pokupateli():
    def __init__(self, familiya, imya, ot4estvo, pasportniedannie, adres, gorod, vozrast, pol):
        self.familiya = familiya
        self.imya = imya
        self.ot4estvo = ot4estvo
        self.pasportniedannie = pasportniedannie
        self.adres = adres
        self.gorod = gorod
        self.vozrast = vozrast
        self.pol = pol
    def info(self):
        print(self.familiya)
        print(self.imya)
        print(self.ot4estvo)
        print(self.pasportniedannie)
        print(self.adres)
        print(self.gorod)
        print(self.vozrast)
        print(self.pol)









# razrabotka modulnogo testirovaniya

import unittest
from Python4lab import Pokupateli


class TestPokupateli(unittest.TestCase):
    def setUp(self):
        self.pok = Pokupateli
unittest.main()





