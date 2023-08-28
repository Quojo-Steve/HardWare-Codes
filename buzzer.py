from gpiozero import Buzzer
from time import sleep

alarm = Buzzer(17)

while True:
    alarm.on()
    sleep(1)
    alarm.off()
    sleep(1)