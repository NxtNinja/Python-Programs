def insertion_sort(list1):
    n = len(list1)
    for i in range(n):
        key = list1[i]
        j = i-1
        while j>=0 and list1[j] > key:
            list1[j+1] = list1[j]
            j = j-1
        list1[j+1] = key


elements = input("Enter a list of numbers (space separated): ").split()

the_list = [int(num) for num in elements]

print("Unsorted: ", the_list)

insertion_sort(the_list)

print(the_list)