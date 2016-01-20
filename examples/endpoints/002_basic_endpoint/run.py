import parlay
import time

# because the start() method doesn't return. We need to define all of our endpoints before we call it.
# we could also define them in different files and import them above.

# THis decorator defines a local endpoint and auto_connects it to the parlay system on startup
@parlay.local_item(auto_connect=True)
class Adder(parlay.ParlayCommandItem):

    @parlay.parlay_command()
    def echo(self, text):
        """
        Will Echo whatever was sent to the python console
        """
        print text
        self.sleep(1)

    @parlay.parlay_command()
    def add(self, x, y):
        """
        Will add x and y and then return and echo the result
        """
        # since python doesnt have type information, we can't know what type the parameters should be
        # so they're always strings that need to be casted
        result = int(x) + int(y)
        self.echo(result)

        return result

    @parlay.parlay_command()
    def error_if_negative(self, x):
        """
        will error out if nagative
        """
        if int(x) < 0:
            raise ValueError("X is NEGATIVE!")


parlay.start()
