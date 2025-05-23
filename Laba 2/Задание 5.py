class MyClass:
    def __init__(self, prop1=0, prop2="Default"):
        self.prop1 = prop1
        self.prop2 = prop2
        print("Объект создан.")

    def __del__(self):
        print(f"Объект удален (prop1={self.prop1}, prop2={self.prop2}).")

    def display_properties(self):
        print(f"Свойство 1: {self.prop1}")
        print(f"Свойство 2: {self.prop2}")

if __name__ == "__main__":

    obj1 = MyClass()
    print("Объект 1 (свойства по умолчанию):")
    obj1.display_properties()

    obj2 = MyClass(10, "Hello")
    print("nОбъект 2 (с заданными свойствами):")
    obj2.display_properties()

    del obj1
    del obj2