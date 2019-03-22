from time import *

LOC_TIME=localtime()
L_HOUR=localtime().tm_hour
L_MINUTE=localtime().tm_min
L_DAY=localtime().tm_wday
L_MONTH=localtime().tm_mon

def checkTheDay()
	if (L_DAY>=0 && L_DAY<=5):
		return 1
	else:
		return 0

def checkIfIsTime(x)
	if(x==1 && L_HOUR==7 && L_MINUTE<35 && L_MINUTE>25):
		return 1
	elif((x==0 && L_HOUR==10 && L_MINUTE<25 && L_MINUTE>10):
		return1
	else:
		return 0

def main()
	if checkIfIsTime())==1:
		#do it
		return
