def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a*b // gcd(a, b)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = lcm(num1, num2)

print("LCM of",num1,"and",num2,"is:",result)