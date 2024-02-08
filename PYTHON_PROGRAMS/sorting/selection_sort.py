def selection_sort(list1):
    n = len(list1)

    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if list1[j] < list1[min_index]:
                min_index = j
        temp = list1[i]
        list1[i] = list1[min_index]
        list1[min_index] = temp



elements = input("Enter a list of numbers (space separated): ").split()

the_list = [int(num) for num in elements]

print("Unsorted: ", the_list)

selection_sort(the_list)

print(the_list)