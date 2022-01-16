#1
# from time import sleep
# from itertools import cycle
#
#
# class TrafficLight:
#
#     def __init__(self):
#         self.__color = (('Red', 3), ('Yellow', 2), ('Green', 5))
#
#     def running(self):
#         for color, sec in cycle(self.__color):
#             print(color, '(wait {} sec)'.format(sec))
#             sleep(sec)
#
#
# traffic_light = TrafficLight()
# traffic_light.running()

#2


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return mass
my_road = Road(20, 5000)
print(my_road.calc_mass(), 'С‚')
#3

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return self._income_wage + self._income_bonus


pos = Position('Ivan', 'Ivanov', 'senior', {"wage": 15000.54, "bonus": 50000.8})
print(pos.get_full_name())
print(pos.get_total_income())

#4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} is going!'.format(self.name))

    def stop(self):
        print('{} is stoping!'.format(self.name))

    def turn(self, direction):
        print('{} is turning to {}!'.format(self.name, direction))

    def show_speed(self):
        print('Current speed:', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Warning! Your speed is more than max!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('Current speed:', self.speed)
        if self.speed > 40:
            print('Warning! Your speed is more than max!')


class PoliceCar(Car):
    pass


sport_car = SportCar(240, 'Желтая', 'спортиваная машина', False)
town_car = TownCar(140, 'Серая', 'Городская машина', False)
work_car = WorkCar(90, 'черная', 'рабочая машина', False)
police_car = PoliceCar(210, 'синяя', 'полицейская машина', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('left')

#5

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('ручка рисует')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш рисует')


class Handle(Stationery):
    def draw(self):
        print('Маркер рисует')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.draw()
pencil.draw()
handle.draw()