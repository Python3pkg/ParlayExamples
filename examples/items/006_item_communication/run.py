import parlay

# we have multiple items declared in separate files. By simply importing them to the file that starts the
# parlay system, theya re included as if there were defined here
import adder
import multiplier
import combiner

parlay.open_protocol("LocalItemProtocol", Item="Adder")
#start the system
parlay.start()