from gpiozero import Button, Buzzer
from signal import pause

buzz = Buzzer(17)
button = Button(2)

button.when_pressed = buzz.on
button.when_released = buzz.off

pause()