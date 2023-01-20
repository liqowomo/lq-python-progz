#!/usr/bin/env python3

'''
Testing out nice ass os command execution 
'''

import subprocess

# Lets write some simple ass commands

# This is just running a simple command in 1 line
ip_info = subprocess.run(['curl', 'ipinfo.io'], stdout=True)


# Same above command now in a loop

for x in range(5):
    print("Printing the args: ", ip_info.args)  # printing the args
    print("Printing the stdout:",ip_info.stdout)  # Prints nothing
    print("Printingt the returncode:", ip_info.returncode)  # Prints


# Dummy to push comment in

# Just added this line after closing and then opening this with codespaces for testing

# ip_info variable is empty have to make this clear now
