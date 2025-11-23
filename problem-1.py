class Calculator:
    def calculate(self, a, b, operation):
        if operation == "add":
            return a + b
        elif operation == "sub":
            return a - b
        elif operation == "mul":
            return a * b
        elif operation == "div":
            return a / b
        else:
            return "Invalid Operation"


a = float(input("Enter a: "))
b = float(input("Enter b: "))
op = input("Enter operation (add/sub/mul/div): ")

print("Result =", Calculator().calculate(a, b, op))
