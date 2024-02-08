def factorial(num):
    if num <= 1:
        return 1
    elif num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
number = int(input("Enter any number: "))
result = factorial(number)
print("The factorial of number",number, "is:",result)