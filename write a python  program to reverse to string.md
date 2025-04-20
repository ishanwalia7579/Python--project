#write a python  program to reverse to string

#using for slicing :

```py
text=input("Enter a string")
reversed_string=text[::-1]
print("This is reverse string",reversed_string)
```
#output like= 10 11 12 13 14 15<br>
answer is =51 41 31 21 11 01

#Without using slicing (using loop)

```py
text=input("Enter a string")
reversed_text= ""
for char in text:
     reversed_text=char+reversed_text:
print("This reverse string",reversed_text)

```

#output like = 102 201 92 82<br>
answer= 28 29 102 201
