"""
Display the distance on the LCD
"""

from parlay.utils import setup, sleep, get_item_by_name, discover

setup(ip="172.16.42.104")
discover(force=False)

LCD = get_item_by_name("LCD")
# you can wait for complete on a handle if you want
handle = LCD.send_parlay_command("init")
handle.wait_for_complete()

dist = get_item_by_name("DISTANCE_SENSOR")
dist.init()

#get a handle but DONT wait on it to finish since this loops forever
handle = LCD.send_parlay_command("loop")
handle = dist.send_parlay_command("poll_forever")
print("STARTING...")

for i in range(60):
    str_distance = "%.3f" % dist.DISTANCE
    print(str_distance)
    LCD.TEXT = str_distance
    sleep(1)