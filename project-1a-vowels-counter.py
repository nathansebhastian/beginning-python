string = input("Enter a string: ")

vowels = "aeiou"
count = 0
for char in string:
    if char in vowels:
        count += 1

print(f"The string: {string}")
print(f"Number of Vowels: {count}")