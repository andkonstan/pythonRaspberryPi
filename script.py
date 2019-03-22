from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
from temperatureMine import *
from timeModule import *
lcd = Adafruit_CharLCD()

counter=0

lcd.begin(16,1)

while 1:

	if(counter%10==0):
		timeModule.main()
		if(counter==20):
			counter=0
		counter=counter+1

	temp=main()
        lcd.clear()
	lcd.message(datetime.now().strftime('%b %d  %H:%M\n'))
	lcd.message(temp)
	sleep(30)
	lcd.clear()
	lcd.message('You are able! \n')
	lcd.message('You can do this!')
	sleep(7)

