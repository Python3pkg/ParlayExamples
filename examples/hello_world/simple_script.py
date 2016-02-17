from parlay.utils import setup, discover, get_item_by_name

setup()

print "Discovering..."
discover(force=True)
print "Discovery Complete!"

cheerful_person = get_item_by_name("CheerfulPerson")

response = cheerful_person.say_hello()

print response

