class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days
    def get_salary(self):
        salary = self.rate * self.days
        print(f"Зарплата работника {self.name} {self.surname}: {salary}")
if __name__ == "__main__":
    worker1 = Worker("Иван", "Иванов", 1000.0, 20)
    worker1.get_salary()
    worker2 = Worker("Петр", "Петров", 1500.0, 22)
    worker2.get_salary()