class Times:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def __call__(self, number):
        return self.multiplier * number


times2 = Times(2)
times3 = Times(3)

print(f'{times2(5) = }')
print(f'{times3(5) = }')
