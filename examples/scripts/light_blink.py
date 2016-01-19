from parlay.scripts.script import script, setup
import time
setup(ip="192.168.10.84")
script.discover()
e = script.get_endpoint_by_name("RG_LED")
e.init()

for i in range(20):
    e.turn_green()
    time.sleep(1)
    e.turn_red()
    time.sleep(1)