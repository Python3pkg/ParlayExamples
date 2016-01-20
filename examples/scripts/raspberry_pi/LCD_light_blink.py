"""
Blink the light, but display the color on the LCD
"""

from parlay.scripts.script import script, setup
import time
setup(ip="172.16.42.104")
script.discover(force=False)
led = script.get_item_by_name("RG_LED")
led.init()
LCD = script.get_item_by_name("LCD")
handle = LCD.send_parlay_command("init")
handle.wait_for_complete()

#get a handle but DONT wait on it to finish since this loops forever
handle = LCD.send_parlay_command("loop")
print "STARTING..."

for i in range(30):
    LCD.TEXT = "GREEN"
    print LCD.TEXT
    led.turn_green()
    time.sleep(1)
    LCD.TEXT = "RED"
    print LCD.TEXT
    led.turn_red()
    time.sleep(1)