def fibonacci(num):
    sequence = []
    a, b = 0, 1
    count = 0

    while count < num:
        sequence.append(a)
        a, b = b, a + b
        count += 1
    
    return sequence


number = int(input("Enter the number of fibonacci terms you want to see: "))

fib_sequence = fibonacci(number)

print(fib_sequence)

