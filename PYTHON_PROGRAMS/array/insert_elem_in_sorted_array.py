import array

def insert_element(arr, element):
    index = 0
    while index < len(arr) and arr[index] < element:
        index += 1
    arr.insert(index, element)
    return arr

my_array = array.array("i", [1, 2, 3, 4, 6, 7, 8, 9])

print(my_array)

print(insert_element(my_array, 5))

