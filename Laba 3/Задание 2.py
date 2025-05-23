class Worker:
    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days
    def get_name(self):
        return self.__name
    def get_surname(self):
        return self.__surname
    def get_rate(self):
        return self.__rate
    def get_days(self):
        return self.__days
    def get_salary(self):
        salary = self.__rate * self.__days
        print(f"Зарплата работника {self.__name} {self.__surname}: {salary}")
if __name__ == "__main__":
    worker1 = Worker("Иван", "Иванов", 1000.0, 20)
    name = worker1.get_name()
    surname = worker1.get_surname()
    rate = worker1.get_rate()
    days = worker1.get_days()
    print(f"Имя: {name}")
    print(f"Фамилия: {surname}")
    print(f"Ставка: {rate}")
    print(f"Дней: {days}")
    worker1.get_salary()