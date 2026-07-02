import os
os.system("cls")
devices = [
    {"name" : "PLC1" , "location" : "PC17_CTB" , "status" : "online" , "ip" : "192.168.100.10"},
    {"name" : "PLC2" , "location" : "PC17_WP1" , "status" : "online" , "ip" : "192.168.101.10"},
    {"name" : "PLC3" , "location" : "PC17_WP2" , "status" : "online" , "ip" : "192.168.102.10"},
    {"name" : "PLC4" , "location" : "PC17_WP3" , "status" : "offline" , "ip" : "192.168.103.10"},
    {"name" : "HMI1" , "location" : "PC17_CTB" , "status" : "online" , "ip" : "192.168.100.11"},
    {"name" : "HMI2" , "location" : "PC17_WP1" , "status" : "online" , "ip" : "192.168.101.2"},
    {"name" : "HMI3" , "location" : "PC17_WP2" , "status" : "online" , "ip" : "192.168.102.2"},
    {"name" : "HMI4" , "location" : "PC17_WP3" , "status" : "offline" , "ip" : "192.168.103.2"}
]
offline_device = 0
online_device = 0
unknown_device = 0
for device in devices:
    if device['status'].lower() == 'offline':
        print(f"{device['name']} : {device['location']} : {device['ip']} is Offline")
        offline_device += 1
    elif device['status'].lower() == 'online':
        online_device += 1
    else:
        print(f"devices unknown/ not recorded: {unknown_device}")
print(f"devices offline: {offline_device}" )
print(f"devices online: {online_device}")