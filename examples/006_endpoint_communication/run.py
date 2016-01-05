import parlay

# because the start() method doesn't return. We need to define all of our endpoints before we call it.
# we could also define them in different files and import them above.

# THis decorator defines a local endpoint and auto_connects it to the parlay system on startup
@parlay.local_endpoint(auto_connect=True)
class Adder(parlay.ParlayCommandEndpoint):

    @parlay.parlay_command()
    def add(self, x, y):
        """
        Will add x and y and then return and echo the result

        ###Parlay will perform automatic type coercian if possible if the type is specified###

        :type x int
        :type y int
        """
        result = x + y
        self.echo(result)

        return result

@parlay.local_endpoint(auto_connect=True)
class Multiplier(parlay.ParlayCommandEndpoint):

    @parlay.parlay_command()
    def multiply(self, x, y):
        """
        Will add x and y and then return and echo the result

        ###Parlay will perform automatic type coercian if possible if the type is specified###

        :type x int
        :type y int
        """
        result = x * y
        self.echo(result)

        return result

@parlay.local_endpoint(auto_connect=True)
class Combiner(parlay.ParlayCommandEndpoint):

    @parlay.parlay_command()
    def multiply(self, x, y):
        """
        Will add x and y and then return and echo the result

        ###Parlay will perform automatic type coercian if possible if the type is specified###

        :type x int
        :type y int
        """
        result = x * y
        self.echo(result)

        return result




parlay.start()