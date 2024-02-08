def uppercase(name):
    uppercase_name = ""
    for char in name:
        if 97 <= ord(char) <= 122:
            uppercase_name += chr(ord(char) - 32)
        else:
            uppercase_name += char

    return uppercase_name


def lowercase(name):
    lowercase_name = ""
    for char in name:
        if 65 <= ord(char) <= 90:
            lowercase_name += chr(ord(char) + 32)
        else:
            lowercase_name += char

    return lowercase_name


num = int(input("Enter 1 to start and 0 to end: "))

while num == 1:
    name = input("Enter you name: ")
    choice = input("Enter 1 for uppercase and 2 for lowercase")
    match(choice):
        case "1":
            print(uppercase(name))
            pass
        case "2":
            print(lowercase(name))
            pass
        case _:
            print("Please enter valid choice")
            pass

    num = int(input("Enter 1 to start and 0 to end"))