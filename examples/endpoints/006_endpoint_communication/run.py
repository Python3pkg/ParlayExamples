import parlay

# we have multiple endpoints declared in separate files. By simply importing them to the file that starts the
# parlay system, theya re included as if there were defined here
import adder
import multiplier
import combiner

parlay.open_protocol("LocalEndpointProtocol", Endpoint="Adder")
#start the system
parlay.start()