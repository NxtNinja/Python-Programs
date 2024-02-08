def remove_duplicate(arr):
    unique_elemets = array.array("i", [])

    for element in arr:
        if element not in unique_elemets:
            unique_elemets.append(element)
    return unique_elemets


import array

my_array = array.array("i", [2,4,9,2,7,3,7,8,9,10])

print(my_array)

unique_array = remove_duplicate(my_array)

print(unique_array)