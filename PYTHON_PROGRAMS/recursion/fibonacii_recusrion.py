def fibo(num): 
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)
    
number = int(input("Enter the number of terms you want: "))
listA = []

print("Fibonacci series upto",number,"terms:")
for i in range(0, number+1, 1):
    listA.append(fibo(i))

print(listA)