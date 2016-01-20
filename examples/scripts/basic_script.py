from parlay.utils import setup, discover, get_item_by_name

setup()
discover()
e = get_item_by_name("Adder")
print e.add(2,3)