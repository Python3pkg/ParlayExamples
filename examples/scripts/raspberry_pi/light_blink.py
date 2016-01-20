from parlay.utils import discover, get_item_by_name, setup, sleep

setup(ip="172.16.42.104")  # This sets up the scripting environment and tells the script which IP to connect to.
                           # default is localhost

discover()          # Issue a discovery (This must be done before get_item_by_name or get_item_by_id
                    # we won't know what we're connected to!)
rg_led = get_item_by_name("RG_LED")  # Get an item by its name. If its ambiguous, it will return the first one
                                       # use get_item_by_id for unambiguous
rg_led.init()  # issue commands by calling them like functions (They can take arguments too)
          # commands called this way will BLOCK until they have been completed
          # if an error is returned, it will be raised as a BadStatusException()

for i in range(20):
    rg_led.turn_green()
    sleep(1)
    rg_led.turn_red()
    sleep(1)