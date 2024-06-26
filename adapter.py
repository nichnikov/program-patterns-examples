"""
https://github.com/pkolt/design_patterns/blob/master/structural/adapter.py
"""

# coding: utf-8

"""

Адаптер - паттерн, структурирующий классы и объекты.

Преобразует интерфейс одного класса в интерфейс другого, который ожидают клиенты.
Адаптер обеспечивает совместную работу классов с несовместимыми интерфейсами, которая без него была бы невозможна.

"""


class Dog(object):
    def __init__(self, name):
        self._name = name

    def bark(self):
        return '%s: гав-гав!' % self._name


class Cat(object):
    def __init__(self, name):
        self._name = name

    def meow(self):
        return '%s: мяу-мяу!' % self._name


class CatAdapter(Dog):
    # благодаря адаптеру мы можем использовать
    # интерфейс класса `Dog`, а реализацию класса `Cat`.

    def __init__(self, name):
        super(CatAdapter, self).__init__(name=name)
        self._cat = Cat(name=name)

    def bark(self):
        # запрос `bark` преобразуется в запрос `meow`
        return self._cat.meow()

if __name__ == "__main__":
    dog = Dog('Тузик')
    print(dog.bark())  # Тузик: гав-гав!

    cat_adp = CatAdapter('Тузик') # т. е. класс Dog адаптируется для класса Cat используя адаптер CatAdapter, выдавая мяу
    print(cat_adp.bark())  # Тузик: мяу-мяу!``

    cat = Cat("Барсик")
    print(cat.meow())