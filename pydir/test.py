#!/usr/bin/env python3

'''
Testing out nice ass os command execution 
'''

import subprocess

# Lets write some simple ass commands 

ip_info = subprocess.run(['curl', 'ipinfo.io'])