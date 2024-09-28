class Tugiac:
    def __init__(self, width1, width2, width3, width4):
        self.width1 = width1
        self.width2 = width2
        self.width3 = width3
        self.width4 = width4
    def __str__(self):
        return f"{self.width1}x{self.width2}x{self.width3}x{self.width4}"
class Tamgiac:
    def __init__(self, width1, width2, width3):
        self.width1 = width1
        self.width2 = width2
        self.width3 = width3
    def __str__(self):
        return f"{self.width1}x{self.width2}x{self.width3}"
    def Chuvi(self):
        return self.width1 + self.width2 + self.width3
class Hinhvuong(Tugiac):
    def __init__(self, width1):
        super().__init__(width1, width1, width1, width1)
    def __str__(self):
        return f"{self.width1}x{self.width1}x{self.width1}x{self.width1}"
    def Chuvi(self):
        return self.width1 * 4
    def DienTich(self):
        return self.width1 * self.width1
class Hinhchunhat(Tugiac):
    def __init__(self, width1, width2):
        super().__init__(width1, width2, width1, width2)
    def __str__(self):
        return f"{self.width1}x{self.width2}x{self.width1}x{self.width2}"
    def Chuvi(self):
        return (self.width1 + self.width2) * 2
    def DienTich(self):
        return self.width1 * self.width2
class Hinhbinhhanh(Tugiac):
    def __init__(self, width1, width2, width3): 
        super().__init__(width1, width2, width3, width3)
    def __str__(self):
        return f"{self.width1}x{self.width2}x{self.width1}x{self.width2}"     
    def DienTich(self):
        return (self.width1*self.width3)/2
    def Chuvi(self):
        return (self.width1 + self.width2)*2
class Hinhthang(Tugiac):
    def __init__(self, width1, width2, width3, width4, chieucao):
        super().__init__(width1, width2, width3, width4)
        self.chieucao = chieucao
    def __str__(self):
        return f"{self.width1}x{self.width2}x{self.width3}x{self.width4}"
    def Chuvi(self):
        return (self.width1 + self.width2 + self.width3 + self.width4)
    def DienTich(self):
        return (self.width1+self.width2)*self.chieucao/2
class Hinhthoi(Tugiac):
    def __init__(self, width1, dc1, dc2):
        super().__init__(width1, width1, width1, width1)
        self.dc1 = dc1
        self.dc2 = dc2
    def __str__(self):
        return f"{self.width1}x{self.width1}x{self.width1}x{self.width1}"
    def Chuvi(self):
        return self.width1 * 4
    def DienTich(self):
        return (self.dc1 * self.dc2)/2
def main():
    while True:
        print("0. Tamgiac")
        print("1. Hinh vuong")
        print("2. Hinh chu nhat")
        print("3. Hinh binh hanh")
        print("4. Hinh thang")
        print("5. Hinh thoi")
        print("6. Thoat")
        chon = int(input("Chon chuc nang: "))
        if chon == 1:
            print("Hinh vuong")
            width1 = float(input("width1: "))
            hinhvuong = Hinhvuong(width1)
            print(hinhvuong)
            print(hinhvuong.Chuvi())
            print(hinhvuong.DienTich())
        elif chon == 2:
            print("Hinh chu nhat")
            width1 = float(input("width1: "))
            width2 = float(input("width2: "))
            hinhchunhat = Hinhchunhat(width1, width2)
            print(hinhchunhat)
            print(hinhchunhat.Chuvi())
            print(hinhchunhat.DienTich())   
        elif chon == 3:
            print("Hinh binh hanh")
            width1 = float(input("width1: "))
            width2 = float(input("width2: "))
            width3 = float(input("width3: "))
            hinhbinhhanh = Hinhbinhhanh(width1, width2, width3)
            print(hinhbinhhanh)
            print(hinhbinhhanh.Chuvi())
            print(hinhbinhhanh.DienTich())
        elif chon == 4:
            print("Hinh thang")
            width1 = float(input("width1: "))
            width2 = float(input("width2: "))
            width3 = float(input("width3: "))
            width4 = float(input("width4: "))
            chieucao = float(input("chieu cao: "))
            hinhthang = Hinhthang(width1, width2, width3, width4, chieucao)
            print(hinhthang)
            print(hinhthang.Chuvi())
            print(hinhthang.DienTich())
        elif chon == 5:
            print("Hinh thoi")
            width1 = float(input("width1: "))
            dc1 = float(input("dc1: "))
            dc2 = float(input("dc2: "))
            hinhthoi = Hinhthoi(width1, dc1, dc2)
            print(hinhthoi)
            print(hinhthoi.Chuvi()) 
            print(hinhthoi.DienTich())
        elif chon == 6:
            break
        elif chon == 0:
            print("Tamgiac")
            width1 = float(input("width1: "))
            width2 = float(input("width2: "))
            width3 = float(input("width3: "))
            tamgiac = Tamgiac(width1, width2, width3)
            print(tamgiac)
            print(tamgiac.Chuvi())
main()
        