from parlay.utils import discover, setup, get_item_by_name
# run 006_endpoint_communication for this
setup()
discover()
e = get_item_by_name("Adder")
print e.error_if_negative(-2)