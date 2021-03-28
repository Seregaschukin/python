# 4. Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.
class Car:

    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'{self.name} цвет {color}')

    def go(self):
        return f'{self.name} поехала'
    def stop(self):
        return f'{self.name} остановилась'
    def turn(self, direction):
        self.direction = direction
        return f'{self.name} повернула {self.direction}'
    def show_speed(self):
        return f'{self.name} едет со скоростью {self.speed} км/ч'

class TownCar(Car):
    speed_limit = 60
    def show_speed(self):

        if self.speed < self.speed_limit:
            return (f'{self.name} едет со скоростью {self.speed} км/ч')
        elif self.speed > self.speed_limit:
            return (f'{self.name} едет со скоростью {self.speed} км/ч, превышает на {self.speed - self.speed_limit}  км/ч')

class SportCar(Car):
    pass

class WorkCar(Car):
    speed_limit = 40
    def show_speed(self):
        if self.speed < self.speed_limit:
            return (f'{self.name} едет со скоростью {self.speed} км/ч')
        elif self.speed > self.speed_limit:
            return (f'{self.name} едет со скоростью {self.speed} км/ч, превышает на {self.speed - self.speed_limit}  км/ч')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_polic):
        super().__init__(speed, color, name, is_polic)

mus = PoliceCar(50, 'green', 'LADA', True)
mus_1 = WorkCar(90, 'red', 'BMW', False)
mus_2 = TownCar(70, 'yellow', 'Volvo', False)
print('')
print(mus.go())
print(mus.show_speed())
print(mus.turn('направо'))
print(mus.stop())
print(mus.is_police)
print('')

print(mus_1.go())
print(mus_1.show_speed())
print(mus_1.turn('налево'))
print(mus_1.stop())
print('')

print(mus_2.go())
print(mus_2.show_speed())
print(mus_2.turn('налево'))
print(mus_2.stop())
print('')
