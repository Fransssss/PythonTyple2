# tuple = ordered and unchangeable group of related data

meat = ["pork", "chicken", "pork", "beef", "chicken"]
vegetable = ["Brocoli", "Spinach", "Brocoli", "tomato", "tomato"]

print("\n== Tuple Statement ==")
print("1. Display data")
print("2. Count a word in list")
print("3. Locate the index of a word in list")
print("E. Exit")
choice = input("choice: ")

while choice != 'e' and choice != 'E':
    if choice == "1":
        print("\nDisplay Data")
        print(meat)
        print(vegetable)
    elif choice == "2":
        print("\tCount a word in list")
        list = input("\ta. 1st Data\n\tb. 2nd Data\n\tchoice: ")
        if list == 'a':
            word = input("\tinput a word to count: ")
            print("\tcount: " + str(meat.count(word)))
        elif list == 'b':
            word = input("\tinput a word to count: ")
            print("\tcount: " + str(vegetable.count(word)))
        else:
            print("\t[invalid input]")
    elif choice == "3":
        print("\tLocate the index of a word in list")
        list = input("\ta. 1st Data\n\tb. 2nd Data\n\tchoice: ")
        if list == 'a':
            word = input("\tinput a word to locate: ")
            print("\tlocation: " + str(meat.index(word)))
        elif list == 'b':
            word = input("\tinput a word to locate: ")
            print("\tlocation: " + str(vegetable.index(word)))
        else:
            print("\t[invalid input]")
    else:
        print("\n[Invalid input]")

    print("\n== Tuple Statement ==")
    print("1. Display data")
    print("2. Count a word in list")
    print("3. Locate the index of a word in list")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")