# 3. Реализовать базовый класс Worker (работник).
#
#     определить атрибуты: name, surname, position (должность), income (доход);
#     последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
#     оклад и премия, например, {"wage": wage, "bonus": bonus};
#     создать класс Position (должность) на базе класса Worker;
#     в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
#     и дохода с учётом премии (get_total_income);
#     проверить работу примера на реальных данных: создать экземпляры класса Position,
#     передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def info(self):
        get_total_income = 0
        for i in self._income.values():
            get_total_income += i
        get_full_name = f'{self.name} {self.surname}, доход: {get_total_income}'
        return get_full_name

woker_1 = Position('Иван','Иванов','Президент',500,50)
woker_2 = Position('Петров','Петр','Грузчик',750,75)
print(woker_1.info())
print(woker_2.info())
