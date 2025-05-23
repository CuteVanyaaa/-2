class NumberPair:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def display(self):
        print(f"Первое число: {self.num1}")
        print(f"Второе число: {self.num2}")

    def change_numbers(self, new_num1, new_num2):
        self.num1 = new_num1
        self.num2 = new_num2
        print("Значения чисел успешно изменены.")
    def calculate_sum(self):
        return self.num1 + self.num2
    def find_max(self):
        return max(self.num1, self.num2)

if __name__ == "__main__":
    pair = NumberPair(10, 5)

    print("Исходные значения:")
    pair.display()

    pair.change_numbers(20, 15)

    print("nНовые значения:")
    pair.display()

    sum_of_numbers = pair.calculate_sum()
    print(f"nСумма чисел: {sum_of_numbers}")

    max_value = pair.find_max()
    print(f"Наибольшее значение: {max_value}")