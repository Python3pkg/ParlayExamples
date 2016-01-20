from parlay.scripts.script import script, setup

setup()
script.discover()
e = script.get_item_by_name("Adder")
print e.add(2,3)