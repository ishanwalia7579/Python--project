#Write a python program to find the common character between two string

```py

str1=input("Enter  a first string")
str2=input("Enter a second string")
common= " "
for char in str1:
    if char in str2 and char not in common:
                    common+=char
print("Common character :",common)

```
