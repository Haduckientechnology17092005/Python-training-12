class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __str__(self):
        terms = []
        for i, coeff in enumerate(self.coefficients):
            if coeff != 0:
                if i == 0:
                    term = f"{coeff}"
                elif i == 1:
                    term = f"{coeff}x"
                else:
                    term = f"{coeff}x^{i}"
                if term not in terms:
                    terms.append(term)
        return " + ".join(terms) if terms else "0"

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coeffs = [0] * max_len
        for i in range(max_len):
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs[i] = coeff1 + coeff2
        return Polynomial(new_coeffs)

    def __sub__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coeffs = [0] * max_len
        for i in range(max_len):
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs[i] = coeff1 - coeff2
        return Polynomial(new_coeffs)

    def __mul__(self, other):
        new_coeffs = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                new_coeffs[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(new_coeffs)

    def __truediv__(self, other):
        """Chia hai đa thức (kiểm tra chia cho 0)"""
        if len(other.coefficients) == 1 and other.coefficients[0] == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        elif len(other.coefficients) == 1:
            new_coeffs = [coeff / other.coefficients[0] for coeff in self.coefficients]
            return Polynomial(new_coeffs)
        else:
            raise ValueError("Chỉ có thể chia với một đa thức bậc 0.")

# Ví dụ sử dụng lớp Polynomial
p1 = Polynomial([1, 2, 3, 5, 8])  # 1 + 2x + 3x^2
p2 = Polynomial([4, 0, 1, 4])  # 4 + 0x + 1x^2

print("Đa thức p1:", p1)
print("Đa thức p2:", p2)

# Cộng đa thức
p3 = p1 + p2
print("p1 + p2:", p3)

# Trừ đa thức
p4 = p1 - p2
print("p1 - p2:", p4)

# Nhân đa thức
p5 = p1 * p2
print("p1 * p2:", p5)

# Chia đa thức
try:
    p6 = p1 / Polynomial([10])  # Chia p1 cho 1
    print("p1 / 1:", p6)
except ZeroDivisionError as e:
    print(e)
