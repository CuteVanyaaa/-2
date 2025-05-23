class Calculation:
    def __init__(self):
        self.calculationLine = ""
    def set_calculation_line(self, new_line):
        self.calculationLine = new_line
    def set_last_symbol_calculation_line(self, symbol):
        self.calculationLine += symbol
    def get_calculation_line(self):
        return self.calculationLine
    def get_last_symbol(self):
        if self.calculationLine:
            return self.calculationLine[-1]
        else:
            return None
    def delete_last_symbol(self):
        if self.calculationLine:
            self.calculationLine = self.calculationLine[:-1]
if __name__ == "__main__":
    calc = Calculation()
    calc.set_calculation_line("2 + 2 * 2")
    print("Строка вычисления:", calc.get_calculation_line())
    calc.set_last_symbol_calculation_line(" / 2")
    print("Строка вычисления (после добавления символа):", calc.get_calculation_line())
    last_symbol = calc.get_last_symbol()
    print("Последний символ:", last_symbol)
    calc.delete_last_symbol()
    print("Строка вычисления (после удаления последнего символа):", calc.get_calculation_line())
    calc.set_calculation_line("")
    print("nСтрока вычисления (пустая):", calc.get_calculation_line())
    last_symbol = calc.get_last_symbol()
    print("Последний символ (пустая строка):", last_symbol)
    calc.delete_last_symbol()
    print("Строка вычисления (после удаления символа из пустой строки):", calc.get_calculation_line())