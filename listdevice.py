#!/usr/bin/env python

"""
Program:
This program will list devices via adb
History:
20170920 Kuanlin Chen
"""

import shlex
import subprocess

def command_adb_devices():
	cmd = 'adb devices'
	process = subprocess.Popen(shlex.split(cmd),stdout=subprocess.PIPE)
	line = process.stdout.read().split('\n')
	
	if len(line)<4:
		print("There is no device!")
		return None
	elif len(line)>4:
		print("More than one devices are connected!")
		return None
	else:
		serial_no = line[1].split('\t').pop(0)
		return serial_no

if __name__ == '__main__':
	serial_no = command_adb_devices()
	if serial_no is not None:
		print("Serial Number:"+serial_no)
