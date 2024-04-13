def divide(a, b):
    try:
        result = a / b
        print(f"Result of division:{ result}")
    except ZeroDivisionError:
        print("Error: Division by zero!")

divide(10, 2)
divide(5, 0)
