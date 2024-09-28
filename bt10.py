class VietNam:
    name = "Viet Nam"
    danso = 100000000
    dientich = 331212
    def __init__(self):
        self.name = "Viet Nam"
        self.danso = 100000000
        self.area = 331212
    @staticmethod
    def printNationality():
        print(VietNam.name)
    @staticmethod
    def printArea():
        print(VietNam.dientich)
    @staticmethod
    def printPopulation():
        print(VietNam.danso)

VietNam.printNationality()
VietNam.printArea()
VietNam.printPopulation()