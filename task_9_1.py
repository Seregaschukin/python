# 1. Создать класс TrafficLight (светофор).
#
#     определить у него один атрибут color (цвет) и метод running (запуск);
#     атрибут реализовать как приватный;
#     в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#     продолжительность первого состояния (красный) составляет 7 секунд,
#     второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#     переключение между режимами должно осуществляться только в указанном порядке
#     (красный, жёлтый, зелёный);
#     проверить работу примера, создав экземпляр и вызвав описанный метод.
import time

class Traffic_Light:
    __collor = ['красный', 'желтый', 'зеленый']

    def __init__(self, time_red, time_yellow, time_green):
        self.time_red = time_red
        self.time_yellow = time_yellow
        self.time_green = time_green
        self.__collor = self.__collor

    def running(self, zicl):
        for i in range(zicl):
            print(f'Горит {self.__collor[0]}')
            time.sleep(self.time_red)
            print(f'Горит {self.__collor[1]}')
            time.sleep(self.time_yellow)
            print(f'Горит {self.__collor[2]}')
            time.sleep(self.time_green)


sv = Traffic_Light(7, 2, 3)
sv.running(2)
