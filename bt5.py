class Phanso:
    def __init__(self, tu, mau):
        if mau == 0:
            raise ValueError("Mẫu số không được bằng 0.")
        self.tu = tu
        self.mau = mau

    def __str__(self):
        return f"{self.tu}/{self.mau}"

    def __add__(self, other):
        tu = self.tu * other.mau + other.tu * self.mau
        mau = self.mau * other.mau
        return Phanso(tu, mau).giamuoc()  # Rút gọn phân số

    def __sub__(self, other):
        tu = self.tu * other.mau - other.tu * self.mau
        mau = self.mau * other.mau
        return Phanso(tu, mau).giamuoc()  # Rút gọn phân số

    def __mul__(self, other):
        tu = self.tu * other.tu
        mau = self.mau * other.mau
        return Phanso(tu, mau).giamuoc()  # Rút gọn phân số

    def __truediv__(self, other):
        if other.tu == 0:
            raise ZeroDivisionError("Không thể chia cho 0.")
        tu = self.tu * other.mau
        mau = self.mau * other.tu
        return Phanso(tu, mau).giamuoc()  # Rút gọn phân số

    @staticmethod
    def gcd(a, b):
        """Hàm tính GCD (ước chung lớn nhất) của hai số."""
        while b != 0:
            a, b = b, a % b
        return a

    def giamuoc(self):
        """Rút gọn phân số."""
        uoc = self.gcd(self.tu, self.mau)
        return Phanso(self.tu // uoc, self.mau // uoc)  # Sử dụng phép chia nguyên

def main():
    a = Phanso(126, 340)
    b = Phanso(2, 4)   
    print("a/b =", a / b)  # Chia
    print("a + b =", a + b)  # Cộng
    print("a - b =", a - b)  # Trừ
    print("a * b =", a * b)  # Nhân
    print("Rút gọn a =", a.giamuoc())  # Rút gọn phân số a
    print("Rút gọn b =", b.giamuoc())  # Rút gọn phân số b

if __name__ == "__main__":
    main()
