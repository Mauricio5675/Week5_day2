# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string 
magic = "abracadabra"

# a. Retrieve the 5th character.
print(magic[4])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.

# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet = "abcdefghijklmnopqrstuvwxyz"
# a. Extract the letters 'hij'.
print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[0:13:2])
# c. Reverse the entire string using slicing.
print(alphabet[::-1])

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote 
jfk="Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy "
substring = jfk.find("John F. Kennedy")
print(substring)
print(jfk[83:-1])
# Manipulating Words:
# Given the string 
info = "Python is fun. Fun is good. Good is subjective. "
# a. Extract the word 'subjective' without knowing its exact position.
substring = info.find("subjective")
print(substring)
print(info[36:-1])
# b. Extract every third word.
print(info[0:-1:3])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
print(info[::-1])
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
yoda = "MAY THE FORCE BE WITH YOU."
print(yoda.lower())
# String Joining and Splitting:
# Given the list 
motto = ["Make", "haste", "slowly."]
#a. Convert the list into a single string.
joined_list = " ".join (motto)
print(joined_list)
# # b. Now, split the string at every occurrence of the letter 'a'.
split_motto= joined_list.split('a')
print(split_motto)
# Replacing Words:
# Modify the sentence: 
life = "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
newlife = life.replace("busy", "distracted")
print(newlife)
# b. Replace "plans" with "mistakes".
newerlife = life.replace("plans", "mistake")
print(newerlife)

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
repetition = "Iteration" * 7
# Word Search:
# Check if the word "moonlight" appears in the quote: 
freedom = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
substring = freedom.find("moonlight")
print(substring)
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: 
long = "Supercalifragilisticexpialidocious"
print(len(long))

# b. Count the number of times the letter 'i' appears in the same word/phrase.
