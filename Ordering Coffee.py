#a simple interaction of ordering coffee from a fictional coffee shop
#variables have to be defined before they can be used

menu = "Cinnamon Swirl,\nPeppermint Mocha,\nCookie Craze,\nVanilla Bean Mushroom Brew"

print("Hello, welcome to Bathory Coffee. Our specials for today are:\n" + menu)

#decimals are called "floats" and they're just as much of a headache as they are from math class...
#luckily here its rather simple
#if statements relate to the input response in order to specify different amounts/actions to take

drink = input("\nWhat can I get started for you?\n")
if drink == "Cinnamon Swirl":
    price = 6.50
if drink == "Peppermint Mocha":
    price = 6.50
if drink == "Cookie Craze":
    price = 7.30
if drink == "Vanilla Bean Mushroom Brew":
    price = 7.80

#double == is the IS part of the statement: "if drink IS this"
#single = is the action/assignment part of the statement: "then DO/USE this"

size = input("\nWhat size would you like?\n")
if size == "small":
    size_tax = 0.10
if size == "medium":
    size_tax = 0.30
if size == "large":
    size_tax = 0.50
if size == "extra large":
    size_tax = 0.80

#integers, int, cannot be multiplied against strings, str, because strings are words not integers/numbers
#whatever a user inputs becomes a string, regardless if its numbers or letters
#change that by putting the input function inside of int() to turn the user response into an integer/number

quantity = int(input("\nHow many cups would you like?\n"))

#dont forget order of operations; PEMDAS

total = (price + size_tax) * quantity
name = input("\nWhat name should I put on this order for you?\n")

#defined variables that are floats/decimals and integers cannot be added into strings
#use str() to change a float/decimal or an integer into a string to be "tied together" with concatenizing

print("\nThank you, " + name + ", your order total is $" + str(total) + ", and it will be ready in 5-10 minutes.")

