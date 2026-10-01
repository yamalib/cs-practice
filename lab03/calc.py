a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
x = input("Введите действие, которое должен сделать калькулятор: ")
match x:
    case "+":
        res = a + b
    case "-":
        res = a - b
    case _:
        res = "Неопознанное действие"
print(res)
