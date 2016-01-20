"""
Blink the light, but display the color on the LCD
"""

from parlay.utils import discover, get_item_by_name, sleep, setup

setup(ip="172.16.42.104")
discover(force=False)
led = get_item_by_name("RG_LED")
led.init()
LCD = get_item_by_name("LCD")
handle = LCD.send_parlay_command("init")
handle.wait_for_complete()

#get a handle but DONT wait on it to finish since this loops forever
handle = LCD.send_parlay_command("loop")
print "STARTING..."

for i in range(30):
    LCD.TEXT = "GREEN"
    print LCD.TEXT
    led.turn_green()
    sleep(1)
    LCD.TEXT = "RED"
    print LCD.TEXT
    led.turn_red()
    sleep(1)