print("Hello!! My name is Python. I'm glad you can join us. Tell me something about you?")
FirstName = input("What is your first name? ")
LastName = input("What is your Last name? ")
print(f"Hello {FirstName.title()} {LastName.title()}, glad you can join us")
age = int(input("How old are you? "))
if age > 18:
    print("Thanks for joining the comunity! ")
elif age == 18:
    print("Thanks for joining the comunity. please follow the rules! ")
else:
    print("I'm sorry, your are too young for this comunity. ")
print("Want to play a game? ")
number1 = int(input("Pick a number and press enter! "))
number2 = int(input("Guess what! Pick another number! "))
if number1 > number2:
    print("Number 1 is greater than number 2")
elif number1 == number2:
    print("They are the same number sily! ")
else:
    print("Number 2 is greater than number 1 ")
result = number1 + number2
print(f"fun fact, you two number added together are {result}! ")