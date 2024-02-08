import array

def separate(arr):
    even_array = array.array("i",[])
    odd_array = array.array("i",[])

    for num in arr:
        if num % 2 == 0:
            even_array.append(num)
        else:
            odd_array.append(num)
    
    return even_array, odd_array

my_array = array.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9])

even, odd = separate(my_array)

print("Even Array: ", even)
print("Odd Array: ", odd)