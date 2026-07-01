devices = [
    ("PLC1", "online"),
    ("HMI1", "online"),
    ("RTU2", "offline"),
    ("SWITCH1", "online"),
    ("RTU3", "offline"),
]
print("What device do you want to know the status of?")
user_input = input("")
user_input = user_input.upper()
found = False
while not found:
    for name, status in devices:
        if name == user_input:
            print(f"{name} is currently {status}. ")
            found = True
        else: 
            name != user_input
            continue
    if found == False:
        print("Sorry, that device was not found.")
        user_input = input("Please try again")
        user_input = user_input.upper()
    