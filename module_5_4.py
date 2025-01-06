from time import sleep


class House:

    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor
    def go_to(self, new_floor):
        if new_floor <= self.number_of_floor and new_floor > 0:
            # print(f'Едем на {new_floor} этаж')
            for i in range(1, new_floor+1):
                print(i)
                # sleep(0.5)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floor}'
    #равенство
    def __eq__(self, other):
        return self.number_of_floor == other.number_of_floor
    #<
    def __lt__(self, other):
        return self.number_of_floor < other.number_of_floor
    #<=
    def __le__(self, other):
        return self.number_of_floor <= other.number_of_floor
    #>
    def __gt__(self, other):
        return self.number_of_floor > other.number_of_floor
    #>=
    def __ge__(self, other):
        return self.number_of_floor >= other.number_of_floor
    #!=
    def __ne__(self, other):
        return self.number_of_floor != other.number_of_floor
    #добавляем этаж
    def __add__(self, value):
        self.number_of_floor += value
        return self
    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        return self.__add__(value)

    #удаление
    def __del__(self):
        print(f'{self.name} снесён, но он остаётся в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
print()
del h2
del h3
print(House.houses_history)


