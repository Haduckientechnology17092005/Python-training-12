import math
class Tamgiac:
    def __init__(self, width1, width2, width3):
        self.width1 = width1
        self.width2 = width2
        self.width3 = width3
        p = (self.width1 + self.width2 + self.width3) / 2
        self.chieucao = 2*((p*(p-self.width1)*(p-self.width2)*(p-self.width3))**0.5)/self.width3

    def Chuvi(self):
        return self.width1 + self.width2 + self.width3

    def DienTich(self):
        return self.chieucao * self.width3 * 0.5
class Tamgiaccan(Tamgiac): 
    def __init__(self, width1, width2, width3):
        super().__init__(width1, width1, width3) 
class Tamgiacvuong(Tamgiac):
    def __init__(self, width1, width2, width3):
        super().__init__(width1, width2, width3)
class Tamgiacdeu(Tamgiac):
    def __init__(self, width1, width2, width3):
        super().__init__(width1, width1, width1)
def main():
    while True:
        print("1. Tam giac")
        print("2. Tam giac can")
        print("3. Tam giac vuong")
        print("4. Tam giac deu")
        print("5. Thoat")
        chon = int(input("Chon chuc nang: "))
        if chon == 1:
            print("Tam giac")
            width1 = float(input("width1: "))
            width2 = float(input("width2: "))
            width3 = float(input("width3: "))
            tamgiac = Tamgiac(width1, width2, width3)
            print(tamgiac)
            print(tamgiac.Chuvi())
            print(tamgiac.DienTich())
        elif chon == 2:
            print("Tam giac can")
            width1 = float(input("width1: "))
            width3 = float(input("width3: "))
            tamgiaccan = Tamgiaccan(width1, width1, width3)
            print(tamgiaccan) 
            print(tamgiaccan.Chuvi())
            print(tamgiaccan.DienTich())
        elif chon == 3:
            print("Tam giac vuong")
            width1 = float(input("width1: "))
            width2 = float(input("width2: "))
            width3 = float(input("width3: "))
            tamgiacvuong = Tamgiacvuong(width1, width2, width3)
            print(tamgiacvuong)
            print(tamgiacvuong.Chuvi())
            print(tamgiacvuong.DienTich())
        elif chon == 4:
            print("Tam giac deu")
            width1 = float(input("width1: "))
            tamgiacdeu = Tamgiacdeu(width1, width1, width1)
            print(tamgiacdeu)
            print(tamgiacdeu.Chuvi())
            print(tamgiacdeu.DienTich())
        elif chon == 5:
            break

if __name__ == "__main__":
    main()