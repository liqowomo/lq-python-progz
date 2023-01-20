#!/usr/bin/env python3

'''
Testing out nice ass os command execution 
'''

import subprocess

# Lets write some simple ass commands

# This is just running a simple command in 1 line
ip_info = subprocess.run(['curl', 'ipinfo.io'])
print("#####################################################")
# This gives peculiar formatting
ip_info_2 = subprocess.run(['curl', 'ipinfo.io'])


# Same above command now in a loop

for x in range(5):
    print("------------------------------------------------")
    print(ip_info)
    print(ip_info_2)


# Dummy to push comment in

# Just added this line after closing and then opening this with codespaces for testing

# ip_info variable is empty have to make this clear now
