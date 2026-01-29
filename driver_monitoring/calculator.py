# calculator.py

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error! Division by zero."
        return x / y

    
if __name__ == "__main__":
    cal = Calculator()
    print(cal.add(2, 4))
    print(cal.subtract(2, 4))
    print(cal.multiply(2, 5))
    print(cal.divide(10, 2))

