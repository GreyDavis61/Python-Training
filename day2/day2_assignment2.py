import os
devices = [
    ("PLC1", "PLC", "online"),
    ("PLC2", "PLC", "offline"),
    ("HMI1", "HMI", "online"),
    ("HMI2", "HMI", "online"),
    ("RTU1", "RTU", "offline"),
    ("RTU2", "RTU", "online"),
    ("RTU3", "RTU", "online"),
    ("SWITCH1", "Network Switch", "online"),
    ("SWITCH2", "Network Switch", "offline"),
    ("FW1", "Firewall", "online"),
    ("SEP1", "Separator", "online"),
    ("SEP2", "Separator", "offline"),
    ("CTB1", "Tank Battery", "online"),
    ("SWD1", "Saltwater Disposal", "online"),
    ("COMP1", "Compressor", "offline"),
]
device_online = 0
device_offline = 0
for name, type, status in devices:
    if "offline" in status:
        device_offline += 1
    elif "online" in status:
        device_online += 1
print(f"{device_online} devices are online. ")
print(f"{device_offline} devices are offline. ")
print(F"{device_offline + device_online} total devices. ")
answer1 = input("would you like to continue? (y/n) ")
answer1 = answer1.upper()
while answer1 != "Y" and answer1 != "N":
    answer1 = input("Please type either a y or n: ")
    answer1 = answer1.upper()
if answer1 == "N":
    os.system('cls')
finished = False
while not finished:
    found = False
    while not found:
        device1 = input("What device do you want the status of? ")
        device1 = device1.upper()
        for name, type, status in devices:
            if name == device1:
                print(f"{name} is currently {status}. ")
                found = True
            else: 
                name != answer1
                continue
        if found == False:
            print("Sorry, that device was not found.")
            answer1 = input("Please try again: ")
            answer1 = answer1.upper()

            
        while answer2 != "Y" and answer2 != "N":
            answer2 = input("Do you want to check another device? (Y/N)")
            answer2 = answer2.upper()
        if answer2 == "N":
                finished = True
                os.system('cls')
