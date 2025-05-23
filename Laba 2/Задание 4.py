class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_value(self):
        return self.value

if __name__ == "__main__":
    counter1 = Counter()
    print("Счетчик 1 (значение по умолчанию):", counter1.get_value())

    counter2 = Counter(10)
    print("Счетчик 2 (произвольное значение):", counter2.get_value())

    counter1.increment()
    counter1.increment()
    print("Счетчик 1 (после увеличения):", counter1.get_value())

    counter2.decrement()
    counter2.decrement()
    counter2.decrement()
    print("Счетчик 2 (после уменьшения):", counter2.get_value())

    counter1.increment()
    counter1.decrement()
    print("Счетчик 1 (после увеличения и уменьшения):", counter1.get_value())

    counter2.decrement()
    counter2.increment()
    counter2.increment()
    print("Счетчик 2 (после уменьшения и увеличения):", counter2.get_value())