class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __lt__(self, other):
        return self.length() < other.length()

vector_a = Vector(2, 2)
vector_b = Vector(3, 0)
print(f'{vector_a = }')
print(f'{vector_b = }')

print(f'{vector_a + vector_b = }')

print(f'{vector_a < vector_b = }')
