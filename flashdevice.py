#!/usr/bin/env python

"""
Program:
This program will list devices via adb
History:
20170920 Kuanlin Chen
"""

import shlex
import subprocess
import time

def run_command(cmd):
	returncode = subprocess.call(shlex.split(cmd),stdout=subprocess.PIPE)
	#return 1 while executing fail
	if(returncode):
		print("Command fail!")
		sys.exit()

def run_command_with_output(cmd):
	process = subprocess.Popen(shlex.split(cmd),stdout=subprocess.PIPE)
	line = process.stdout.read().split('\n')
	for eachline in line:
		print(eachline)

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

def command_reboot_bootloader(serial_no):
	cmd = 'adb -s {} reboot bootloader'.format(serial_no)
	run_command(cmd)

def command_fastboot_devices():
	cmd = 'fastboot devices'
	run_command_with_output(cmd)

def command_fastboot_flash():
	image_path = '/home/kuanlin/TempImage/system.img'
	cmd = 'fastboot flash system {}'.format(image_path)
	run_command_with_output(cmd)

def command_fastboot_reboot():
	cmd = 'fastboot reboot'
	run_command_with_output(cmd)

if __name__ == '__main__':
	serial_no = command_adb_devices()
	if serial_no is not None:
		print("Serial Number:"+serial_no)
		command_reboot_bootloader(serial_no)
		time.sleep(10)
		command_fastboot_devices()
		command_fastboot_flash()
		print("SW Flash completed")
		command_fastboot_reboot()
