import os
devices = [
    ("PLC1", "online"),
    ("HMI1", "online"),
    ("RTU2", "offline"),
    ("SWITCH1", "online"),
    ("RTU3", "offline"),
]
offline_count = 0
for name, status in devices:
    if "offline" in status:
        offline_count += 1
        continue
    print(f"{name} is currently {status}... ")
print(f"you have {offline_count} devices offline. ")
input("press enter to move on. ")
os.system('cls')
found = False
print("What device do you want to know the status of?")
user_input = input("")
user_input = user_input.upper()
for name, status in devices:
    if name != user_input:
        continue
    else: 
        name == user_input
        print(f"{name} is currently {status}. ")
        found = True

