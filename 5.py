def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

number = -10
result = check_number(number)
print(f"The number is: {result}")
