class Person:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'Person({self.data})'

    def __getattr__(self, item):
        return self.data[item]

person1 = Person(dict(name='Sam', age=25))
person2 = Person(dict(name='Alex', age=35))

print(person1)
print(person2)

for person in person1, person2:
    print(f'{person.name} is {person.age} years old')
