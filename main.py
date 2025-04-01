gio = 1.5
mylist = [1, 3]
mari = 1
mylist.insert(1, 4)
print(mylist)
for _ in reversed(range(1, 6)):
    print(_)

if gio == 1.5:
    print('yle var 123')


def hello():
    gio = 1
    gio += 1
    print(gio)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def person_eats(self):
        return f"{self.name} eats"

    def change_person(self):
        self.__age += 19

    def get_age(self):
        return self.__age


p = Person("gio", 17)
# print(p.__age)
p.change_person()
print(p.get_age())
print(gio)
from app import db
db.create_all()
exit()

