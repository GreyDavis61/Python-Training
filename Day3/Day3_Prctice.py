import os
os.system("cls")
devices = [
    {"name": "PLC1", "type": "PLC", "status": "online", "ip": "192.168.1.10"},
    {"name": "RTU2", "type": "RTU", "status": "offline", "ip": "192.168.1.11"},
    {"name": "HMI1", "type": "HMI", "status": "online", "ip": "192.168.1.12"},
]
for device in devices:
    if device['status'] == 'offline':
        print(f"{device['name']} : {device['type']} : {device['ip']}")