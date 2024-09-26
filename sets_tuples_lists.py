#collection = single "variables" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/ Remove Ok. No duplicates.
# Tiple = () ordered and unchangable. Duplicates Ok. FASTER

fruits = ["apple","orange","banana","coconut","kiwi","strawberry","tomato"]
# print(dir(fruits))
# print(help(fruits)) #prints helps

# print(len(fruits)) # prints the amount of words in your list

"apple in fruits"
print("pineapple" in fruits ) #prints true or false if a word is in the list (boolean)

# for fruit in fruits:
#     print(fruit)  (prints the list from top to bottom)

# fruits[0] = "pineapple" # changeing apple to pineapple (reassigns words in list)
# fruits.append("pineapple")
# fruits.remove("apple") #removes word from list
# fruits.insert(0,"pineapple") #adds values in list
# fruits.sort() #sorts the list
# fruits.reverse() #reverses the list
# fruits.clear()