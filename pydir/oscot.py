#!/usr/bin/env python3

'''
Tests of ouptut commands to terminal 
'''

# subprocess package is recommened for

# main package for running system commands 
import subprocess

ip_me = subprocess.Popen(['curl', 'ipinfo.io'], stdout=subprocess.PIPE) #stdout puts it out 
ip_me_jq = subprocess.Popen(['jq'], stdin=ip_me.stdout) # stdin is what we want
