# Loop until user chooses to exit
while True:
    # Ask the user for their choice
    print("Choose an option:")
    print("1. Odd")
    print("2. Even")
    print("3. Exit")
    choice = input("Enter your choice: ")

    # Check the user's choice and perform the corresponding action
    if choice == "1":
        num = int(input("Enter a number: "))
        print(f"Odd numbers from 1 to {num} are:")
        for i in range(1, num+1):
            if i % 2 != 0:
                print(i)
    elif choice == "2":
        num = int(input("Enter a number: "))
        print(f"Even numbers from 1 to {num} are:")
        for i in range(1, num+1):
            if i % 2 == 0:
                print(i)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")