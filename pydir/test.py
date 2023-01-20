#!/usr/bin/env python3

'''
Testing out nice ass os command execution 
'''

import subprocess

# Lets write some simple ass commands 

# This is just running a simple command in 1 line 
ip_info = subprocess.run(['curl', 'ipinfo.io'])

# Same above command now in a loop 

for x in range(5):
    ip_info