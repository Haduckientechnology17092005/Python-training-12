class Hinhbinhhanh:
    def __init__(self, width1, width2, width3): 
        self.width1 = width1
        self.width2 = width2
    def __str__(self):
        return f"{self.width1}x{self.width2}x{self.width1}x{self.width2}"
    def Chuvi(self):
        return (self.width1 + self.width2)*2
class Hinhvuong(Hinhbinhhanh):
    def __init__(self, width1):
        super().__init__(width1, width1, width1)
    def __str__(self):
        return f"{self.width1}x{self.width1}x{self.width1}x{self.width1}"
    def Chuvi(self):
        return self.width1 * 4
    def DienTich(self):
        return self.width1 * self.width1
class Hinhchunhat(Hinhbinhhanh):
    def __init__(self, width1, width2):
        super().__init__(width1, width2, width1)
    def __str__(self):
        return f"{self.width1}x{self.width2}x{self.width1}x{self.width2}"
    def Chuvi(self):
        return (self.width1 + self.width2) * 2
    def DienTich(self):
        return self.width1 * self.width2
def main():
    while True:
        print("1. Hinh vuong")
        print("2. Hinh chu nhat")
        print("3. Thoat")
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
            break
main()