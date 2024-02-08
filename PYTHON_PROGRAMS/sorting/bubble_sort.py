def bubble_sort(user_list):
    n = len(user_list)

    for i in range(n):
        for j in range(0, n-i-1):
            if user_list[j] > user_list[j+1]:
                user_list[j], user_list[j+1] = user_list[j+1], user_list[j]


input_list = input("Enter a list of integers separated by spaces: ").split()

user_list = [int(num) for num in input_list]

print("Unsorted list:", user_list)

bubble_sort(user_list)

print("Sorted list:", user_list)