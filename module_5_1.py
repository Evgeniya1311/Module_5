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

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)