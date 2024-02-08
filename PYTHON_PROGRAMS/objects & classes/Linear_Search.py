class LinearOperation:
    def search(self, num):
        if num in my_list:
            print(num,"is in the list.")
        else:
            print(num,"is not in the list.")

    def sort(self, list1):
        list1.sort()
        print("Soretd List: ", list1)
        

my_list = []
num_elemets = int(input("Enter no. of elements: "))

for i in range(num_elemets):
    element = int(input("Enter element: "))
    my_list.append(element)

print("Updated List: ", my_list)
num = int(input("Enter number you want to find: "))

checkNum = LinearOperation()
checkNum.search(num)
checkNum.sort(my_list)