#Python Program to Sort Words in Alphabetic Order

str1=input("Enter a sentence:")

words = str1.split()

words.sort()

for word in words:
    print(word)
    

# change this value for a different result
my_str = "Hello this Is an Example With cased letters"

# uncomment to take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
