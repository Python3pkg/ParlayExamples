import parlay

parlay.start()
# The above function all will not return until the parlay system is 'shut down' (if ever)
# open a browser on localhost:8080 and see the UI for yourself
# Parlay might complain that it's being run in an insecure DEVELOPER mode. DEVELOPER mode is the default mode and is
# *NOT* secure enough for a production device. BY DESIGN.
# To run in PRODUCTION mode change the above line of code to:
# parlay.start(parlay.Modes.PRODUCTION)
# This disables non-localhost connections so random people can't connect to parlay.