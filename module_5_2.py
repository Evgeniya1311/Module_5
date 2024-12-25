from time import sleep


class House:
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

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))