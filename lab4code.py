import RPi.GPIO as GPIO ## Import library that lets you control the Pi's GPIO pins
from time import sleep ## Import time for delays

GPIO.setwarnings(False) ## Disables messages about GPIO pins already being in use
GPIO.setmode(GPIO.BOARD) ## Indicates which pin numbering configuration to use
pinNumLED = 7
pinNumBTN = 16

GPIO.setup(pinNumLED,GPIO.OUT) ## Tells it that pinNumLED will be outputting
GPIO.setup(pinNumBTN,GPIO.IN) ## Tells it that pinNumBTN will be giving input

## Initialize btnOn and prev_input
btnOn = False
prev_input = 1

while True:
    try:
        input = GPIO.input(pinNumBTN)
        if ((not prev_input) and input):
            btnOn = not btnOn
        prev_input=input
        sleep(0.05)
        
        ## When the button is pressed, start toggling the LED between
        ## HIGH and LOW with a 1s interval between
        if btnOn:
            GPIO.output(pinNumLED,GPIO.HIGH)
            print ('led off...') ## Print that the LED is Off
            sleep(1)
            GPIO.output(pinNumLED,GPIO.LOW)
            print ('led on...') ## Print that the LED is On
            sleep(1)
        else:
            GPIO.output(pinNumLED,GPIO.HIGH)
    except KeyboardInterrupt:
        break
    