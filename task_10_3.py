class Cell:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f'Ячеек {self.x}'

    def __add__(self, other):
        return Cell(self.x + other.x)

    def __sub__(self, other):
        return Cell(self.x - other.x if (self.x - other.x) > 0 else "Разность меньше 0")

    def __mul__(self, other):
        return Cell(self.x * other.x)

    def __floordiv__(self, other):
        return Cell(self.x // other.x)

    def __truediv__(self, other):
        return Cell(round(self.x / other.x, 2))

    def make_order(self, row):
        self.row = row
        res_str = ''
        if self.x > self.row:
            cell_all = self.x
            while cell_all > 0:
                res_str += self.row * '*' + '\n'
                cell_all -= self.row
            if cell_all < 0:
                res_str += abs(cell_all) * '*'
        else:
            res_str += self.x * '*'
        return res_str


cell_1 = Cell(10)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(3))
print(cell_1.make_order(5))
print(cell_2.make_order(6))
