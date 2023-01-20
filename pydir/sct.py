#!/usr/bin/env python3

'''
Now we will try to print out the system commands from a variable
'''

# subprocess package is recommened for

# main package for running system commands
import subprocess

ip_me = subprocess.run(['ss', '-nltp'], capture_output=True, text=True)
curl_color=subprocess.run(['curl', 'ipinfo.io'], capture_output=True, text=True)

print("ip_me output")
print(ip_me.stdout)
print('''
      
      ''')
print("curl_color output")
print(curl_color.stdout)
print('''
      
      ''')