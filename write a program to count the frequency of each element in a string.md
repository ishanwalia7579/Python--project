#write a program to count the frequency of each element in a string

#using dictionary:

```py
# Input from user
text = input("Enter a string: ")

# Create an empty dictionary to store character frequencies
frequency = {}

# Loop through each character in the string
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# Print the frequency of each character
print("Character frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")


```
#answer
```yaml

Enter a string: hello
Character frequencies:
'h': 1
'e': 1
'l': 2
'o': 1

```
