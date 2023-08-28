from gpiozero import LED
from time import sleep

led1 = LED(17)
led2 = LED(23)
led3 = LED(6)

while True:
    led1.on()
    led2.off()
    led3.off()
    sleep(5)
    led1.off()
    led2.on()
    led3.off()
    sleep(5)
    led1.off()
    led2.off()
    led3.on()
    sleep(5)


    
