# calculator_gui.py - Калькулятор з графічним інтерфейсом (українською)
import tkinter as tk
from tkinter import messagebox

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        messagebox.showerror("Помилка", "Ділення на нуль заборонено!")
        return None
    return x / y

def button_click():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation_var.get()
        
        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "×":
            result = multiply(num1, num2)
        elif op == "÷":
            result = divide(num1, num2)
            if result is None:
                return
        
        label_result.config(text=f"Результат: {result}", foreground="#2ecc71")
    except ValueError:
        messagebox.showwarning("Увага", "Будь ласка, вводьте тільки числа!")

# Головне вікно
root = tk.Tk()
root.title("Калькулятор 🇺🇦")
root.geometry("420x550")
root.resizable(False, False)
root.configure(bg="#2c3e50")

# Заголовок
tk.Label(root, text="Простий калькулятор", font=("Arial", 20, "bold"), 
         fg="#ecf0f1", bg="#2c3e50").pack(pady=20)

# Поля вводу
frame = tk.Frame(root, bg="#2c3e50")
frame.pack(pady=10)

tk.Label(frame, text="Перше число:", font=("Arial", 14), fg="#ecf0f1", bg="#2c3e50").grid(row=0, column=0, pady=10, sticky="w")
entry1 = tk.Entry(frame, font=("Arial", 14), width=15, justify="center")
entry1.grid(row=0, column=1, padx=10)

tk.Label(frame, text="Друге число:", font=("Arial", 14), fg="#ecf0f1", bg="#2c3e50").grid(row=1, column=0, pady=10, sticky="w")
entry2 = tk.Entry(frame, font=("Arial", 14), width=15, justify="center")
entry2.grid(row=1, column=1, padx=10)

# Вибір операції
tk.Label(root, text="Оберіть операцію:", font=("Arial", 14), fg="#ecf0f1", bg="#2c3e50").pack(pady=10)
operation_var = tk.StringVar(value="+")
ops = ["+", "-", "×", "÷"]
for i, op in enumerate(ops):
    tk.Radiobutton(root, text=op, variable=operation_var, value=op, 
                   font=("Arial", 18), fg="#e74c3c", bg="#2c3e50", selectcolor="#34495e").pack()

# Кнопка
tk.Button(root, text="Обчислити", font=("Arial", 16, "bold"), bg="#e67e22", fg="white",
          command=button_click, height=2, width=15).pack(pady=30)

# Результат
label_result = tk.Label(root, text="Результат: —", font=("Arial", 18, "bold"), 
                        fg="#3498db", bg="#2c3e50")
label_result.pack(pady=20)

# Підвал
tk.Label(root, text="© 2025 skyragdor | Україна 🇺🇦", font=("Arial", 9), 
         fg="#95a5a6", bg="#2c3e50").pack(side="bottom", pady=15)

root.mainloop()