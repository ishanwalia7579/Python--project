# Program to count words in a string

# Take input from user
text = input("Enter a string: ")

# Split the string into words (by spaces)
words = text.split()

# Count the words
word_count = len(words)

print("Number of words in the string:", word_count)
