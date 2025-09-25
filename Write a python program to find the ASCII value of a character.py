# Prompt the user to enter a character
char = input("Enter a character: ")

# Check if the input is a single character
if len(char) == 1:
    # Use the ord() function to get the ASCII value
    ascii_value = ord(char)
    print(f"The ASCII value of '{char}' is {ascii_value}")
else:
    print("Invalid input. Please enter a single character.")
