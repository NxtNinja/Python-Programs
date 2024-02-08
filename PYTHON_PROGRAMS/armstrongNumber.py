def is_armstrong(num):
    num_str = str(num)

    num_digits = len(num_str)

    armstrong_sum = sum(int(digit)**num_digits for digit in num_str)

    return armstrong_sum == num



number = int(input("Enter a number: "))

if is_armstrong(number):
    print("This is a armstrong number")
else:
    print("This is not an armstrong number")