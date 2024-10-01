#collection = single "variables" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/ Remove Ok. No duplicates.
# Tiple = () ordered and unchangable. Duplicates Ok. FASTER

# fruits = ("apple","orange","banana","coconut","kiwi","strawberry","tomato")

#print(fruits[0:1]) @CANT do this
#print(dir(fruits))
# print(help(fruits)) #prints helps


# print(fruits)

# "apple in fruits"
# print("pineapple" in fruits ) #prints true or false if a word is in the list (boolean)


# fruits[0] = "pineapple" # changeing apple to pineapple (reassigns words in list)
# fruits.append("pineapple")
# fruits.remove("apple") #removes word from list
# fruits.pop #
# fruits.insert(0,"pineapple") #adds values in list
# fruits.sort() #sorts the list
# fruits.reverse() #reverses the list
# fruits.clear() #

#Tiple
# print(len(fruits)) # prints the amount of words in your list
# print(fruits.index("apple")) #find where is apple
# print(fruits.count("coconut")) #count how many of the word is there in the list
# for fruit in fruits:
#      print(fruit)  #(prints the list from top to bottom)


# #looping through the list 
# #otherwise called literating through the list
# cars = ["Chevy","Mercedes","GMC","Ford"]
# for car in cars:
#     #print(len(car))
#     #print(car)
# carRequest = input("add a new car please")
# cars.append(carRequest)
# print(cars)
# print(len(cars))
# print(cars.upper())
# print(cars.upper())
# print(cars)
# if len(cars) > 10:
#     break

# dictionary = a collection of {key:value} pairs
#     ordered and changeable. No duplicates 
capitals = {"USA":"Washington D.C.", "India":"New Delhi", "China":"Beijing","Russia":"Moscow"}
# # print(dir(capitals))
# # print(help(capitals))

# # print(capitals.get("USA"))
# # if capitals.get("USA"):
# #     print("That capital exists")
# # else:
# #     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()
# print(capitals)

# keys = capitals.keys()
# for key in capitals.key():
#     print(key)

# values = capitals.values()
# for vaule in capitals.vaules():
#     print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{value}: {value}")