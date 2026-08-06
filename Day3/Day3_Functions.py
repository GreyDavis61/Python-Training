import os
os.system("cls")
#what is a fuction?? it's like an AOI
def greet(name):
    print(f"hello {name}!")   

greet("Grey")
greet("Austin")
greet("Tyler")

input("Press Enter to continue: ")
os.system('cls')
# this funtion is doing math. I put the values in at the bottom
# and it preforms said math.
def add(number1, number2):
    result = number1 + number2
    return result
answer = add(5,3)
print(answer)

input("Press enter to continue: ")
os.system('cls')
#let's use a fuction for real now...
def device_status(device_type, status):
    device_type = input("What device do you want to check up on? ")
    status = input("What is the status of this device")
    return print(f"{'device_type'} is currently {'status'}...")
device_status