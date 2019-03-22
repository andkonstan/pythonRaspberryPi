#this script you should run as root
#sudo python name.py

#import necessary libs
import os, glob, time

#load the apropriate loadable kernel modules to kernel
#using os.system command
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

#change cuurent working directory to /sys/bus/w1/devices/
#not really usefull
#base_dir= '/sys/bus/w1/devices'

#this is the device folder not really necessary as we know the full path to the file
#we use
#device_folder= '/sys/bus/w1/devices/28-0000054cd214'

#this is the file the device is exporting data
device_file= '/sys/bus/w1/devices/28-0000054cd214/w1_slave'


#method to try and read them temps
def read_temp_raw():
	f= open(device_file, 'r')
	lines= f.readlines()
	f.close()
	return lines

#ready to read them temps and convert
def read_temp():
	lines=read_temp_raw()
	while lines[0].strip()[-3:] !='YES':
		time.sleep(0.2)
		lines = read_temp_raw()
	equals_pos= lines[1].find('t=')
	if equals_pos != -1:
		temp_string = lines[1][equals_pos+2:]
		temp_c = float(temp_string) / 1000.0
		#temp_f = temp_c * 9.0 / 5.0 + 32.0
		return "Feels like %s C" %temp_c
#, temp_f

#print the fucking temperature in f and c
def main():
	return read_temp()
