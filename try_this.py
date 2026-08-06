import os
import re

os.system("cls")
sites = ["PC17", "BD18", "Avalon", "Corral Canyon", "Queen"]

print(sites[2])

sites.append("Loco Hill")
print(sites[5])

print(len(sites))

print(input("Ready to continue? "))
os.system("cls")

site_status = {
    "PC17": "producing",
    "BD18": "shut-in",
    "Avalon": "producing",
    "Corral Canyon": "producing",
    "Queen": "down"
}

print(site_status["BD18"])
print(site_status["Queen"])
site_status["Queen"] = "producing"
print(site_status["Queen"])
site_status["local Hill"] = "down"
print(input("Press Continue to view all sites and their status. "))
os.system("cls")

for site, status in site_status.items():
    print(site, status)
print(input(""))
os.system("cls")

def site_report(site,status):
    print(site, "is currently", status)
result = site_report("BD18", "shut-in")
print(input(""))
os.system("cls")
for site, status in site_status.items():
    site_report(site, status)
