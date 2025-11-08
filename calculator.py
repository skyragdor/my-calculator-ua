# calculator.py - Простий калькулятор українською мовою
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Помилка! Ділення на нуль заборонено!"
    return x / y

print("=== Простий калькулятор ===")
print("Підтримувані операції: + - * /")
print("Для виходу введіть 'q'")

while True:
    operation = input("\nВведіть операцію (+ - * /) або 'q' для виходу: ")
    
    if operation == 'q':
        print("Дякую за використання! До зустрічі! 👋")
        break
    
    if operation not in ['+', '-', '*', '/']:
        print("Невірна операція! Спробуйте ще раз.")
        continue
    
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
    except ValueError:
        print("Будь ласка, вводьте тільки числа!")
        continue
    
    if operation == '+':
        print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
    elif operation == '-':
        print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
    elif operation == '*':
        print(f"Результат: {num1} × {num2} = {multiply(num1, num2)}")
    elif operation == '/':
        result = divide(num1, num2)
        print(f"Результат: {num1} ÷ {num2} = {result}")