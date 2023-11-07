from time import sleep
from hal import hal_input_switch as switch
from hal import hal_led as led

switch.init()
led.init()
while True:

    if switch.read_slide_switch() == 0:
        for i in range(100):
            led.set_output(24, 1)  # Turn on the LED
            sleep(0.05)  # Sleep for 0.1 seconds (10 Hz)
            led.set_output(24, 0)  # Turn off the LED
            sleep(0.05)  # Sleep for 0.1 seconds (10 Hz)
        led.set_output(24, 0)  # Turn off the LED
        
    elif switch.read_slide_switch() == 1:
        led.set_output(24, 1)  # Turn on the LED
        sleep(0.1)  # Sleep for 0.1 seconds (10 Hz)
        led.set_output(24, 0)  # Turn off the LED
        sleep(0.1)  # Sleep for 0.1 seconds (10 Hz)
        i=0
