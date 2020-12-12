#!/usr/bin/python3.7
# Author: Parissa Bakhshi
# Project: Reading sshd_config file


# Removing commented and empty lines. 
# Converting configurable items into members of a list

config_list = []
with open ("/etc/ssh/sshd_config") as ssh_file:
    for line in ssh_file:
        if not line.startswith("#") and not line == "\n":
            config_list.append(line.split())

#Converting list items into a dictionary. The 1st member is the "key" and the other members are the values in the form of a list. 
config_dict = {}
for list_member in config_list:
    config_dict[list_member[0]] = (list_member[1:])
######## All done!
#print (config_dict)
#print (config_dict.values())
#print (config_dict.keys())
# Printing the dictionary

for key,value in config_dict.items():
    config=""
    for i in value:
        config += i + " "
    print("-"*50)
    print(f"{key} ==> {config}")




