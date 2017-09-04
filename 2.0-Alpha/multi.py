#!/usr/bin/env python3
'''quick and dirty script to run subzero on multiple targets in list.txt. 
requires subzero bash alias for subzero.py'''
import subprocess

targets = open('list.txt').readlines()
targets = [i.strip() for i in targets]
for i in targets:
	subprocess.check_call('subzero {}'.format(i),shell=True)

