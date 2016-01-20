from parlay.scripts.script import script, setup
import time
setup(ip="172.16.42.104")  # This sets up the scripting environment and tells the script which IP to connect to.
                           # default is localhost
script.discover()          # Issue a discovery
e = script.get_item_by_name("RG_LED")  # Get an item by its name. If its ambiguous, it will return the first one
                                       # use get_item_by_id for unambiguous
e.init()  # issue commands by calling them like functions (They can take arguments too)
          # commands called this way will BLOCK until they have been completed
          # id an error is returned. it will turn into a BadStatusException() and be raised

for i in range(20):
    e.turn_green()
    time.sleep(1)
    e.turn_red()
    time.sleep(1)