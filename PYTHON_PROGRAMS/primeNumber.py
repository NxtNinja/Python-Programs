def is_prime(num):
    if num <= 1:
        return False
    
    elif num <= 3:
        return True
    
    elif num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5
    while i*i <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6
    
    return True




number = int(input("Enter number to check if it is prime: "))

if is_prime(number):
    print("This is a prime number.")
else:
    print("This is not a prime number.")