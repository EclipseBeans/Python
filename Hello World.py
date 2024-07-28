#hashtag marks the line as a "human comment" so its not read as code and ignored
#removing the # will unmark the line to be read in the script

#print is a function that tells computer to say something
#anything that is put between quotations "" is called a string

#print("hello world")

#to have multiple, separate lines with one print function, \n is used as a line break

#print("hello world\nhello world\nhello world\n")

#putting a space after the \n will have the second and third lines one space indented
#remember space is a character
#alternatively it can be written like:

#print("hello world\n" + "hello world\n" + "hello world")

#the separate strings "" are concatenized, or added together, with a plus sign
#so it tells the computer print, or say, "this" AND "this" AND "this"


#input is for the user to provide an answer/input something- for example, their name
#if you want the code to ask for a user's name AND be able to "remember", we start with an input function

#input("what is your name? ")

#the space afterward is so their input isn't smashed together with the question since a space is a character
#to start a new line for them to type their input, just put \n

#input("what is your name?\n")

#if input is put within the print function like so:

#print(input("what is your name?\n"))

#the input name will be printed to repeat it back to the user because we telling the computer to say what they input
#lets write a simple back and forth where the computer asks for name and then says hello with their name
#to do that, we need to set "name" as a variable like so:

#name = input("What is your name?\n")

#setting th variable will /become/ the input prompt AND set the user's answer as the variable we defined- "name"
#after that, we concatenize, or add, the variable with what we want the computer to say
#this is done with a + sign and since the variable is just the word name, we don't add anything to that

name = input("What is your name?\n")
print("Hello, " + name)

#the printed reply is split with "Hello " and the user's name they gave us is added on with + name
#this works even if the user puts in numbers for their name because their input becomes a string ""
