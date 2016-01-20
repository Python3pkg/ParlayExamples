import parlay

# because the start() method doesn't return. We need to define all of our items before we call it.
# we could also define them in different files and import them above.

# This decorator defines a local item and auto_connects it to the parlay system on startup
@parlay.local_item(auto_connect=True)
class Adder(parlay.ParlayCommandItem):
                               # all of these parameters are optional, but recommended to
    x = parlay.parlay_property(default=0, val_type=int)
    y = parlay.parlay_property(default=0, val_type=int)
    result = parlay.parlay_property(default=0, val_type=int)

    @parlay.parlay_command()
    def echo(self, text):
        """
        Will Echo whatever was sent to the python console
        """

        print text

    @parlay.parlay_command()
    def add(self):
        """
        Will add x and y and then return and echo the result
        """
        self.result = self.x + self.y
        self.echo(self.result)

        return self.result


parlay.start()