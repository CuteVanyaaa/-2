class Train:

    def __init__(self, destination, train_number, departure_time):

        self.destination = destination
        self.train_number = train_number
        self.departure_time = departure_time

    def display_info(self):
        print(f"Пункт назначения: {self.destination}")
        print(f"Номер поезда: {self.train_number}")
        print(f"Время отправления: {self.departure_time}")


def find_train_by_number(trains, train_number):
    for train in trains:
        if train.train_number == train_number:
            return train
    return None

if __name__ == "__main__":
    train1 = Train("Москва", "012A", "10:00")
    train2 = Train("Санкт-Петербург", "345B", "14:30")
    train3 = Train("Казань", "678C", "18:00")

    trains = [train1, train2, train3]

    print("Информация о всех поездах:")
    for train in trains:
        train.display_info()
        print("-" * 20)

    search_number = input("Введите номер поезда для поиска: ")

    found_train = find_train_by_number(trains, search_number)

    if found_train:
        print("Найден поезд:")
        found_train.display_info()
    else:
        print("Поезд с таким номером не найден.")
