import parlay

# because the start() method doesn't return. We need to define all of our endpoints before we call it.
# we could also define them in different files and import them above.

# THis decorator defines a local endpoint and auto_connects it to the parlay system on startup
@parlay.local_endpoint(auto_connect=True)
class Adder(parlay.ParlayCommandEndpoint):

    @parlay.parlay_command()
    def echo(self, text):
        """
        Will Echo whatever was sent to the python console
        """

        print text

    @parlay.parlay_command()
    def add(self, x, y):
        """
        Will add x and y and then return and echo the result
        """
        result = int(x) + int(y)
        self.echo(result)

        return result


parlay.start()