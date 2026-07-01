for step_1 in range(1 , 21):
    print(step_1)
input("Ready to continue? ")


for step_2 in range(0,51,2):
    print(step_2)
input("Ready to continue? ")


print("let's play a game, pick a number between 1 and 10 ")
user1 = int(input("pick a number between 1 through 10: "))
while user1 != 6:
    if user1 > 10:
        user1 = int(input("Please guess something inside 1 - 10: "))
    elif user1 < 1:
        user1 = int(input("Please guess something inside 1 - 10: "))
    elif user1 != 6:
        user1 = int(input("Please try again: "))
    else:
        break
print("You got it!")
input("Ready to continue? ")


devices = ["PLC1","HMI1","OFFLINE_RTU3","Switch1"]
for device in devices:
    if "OFFLINE" in device:
        continue
    print(f"Pinging {device}... ")
input("Ready to continue? ")

for stage_3 in range(1 , 16):
    if stage_3 == 13:
        break
    elif (stage_3 % 3) == 0:
        print("Divisible by 3")
    else:
        print(stage_3)
