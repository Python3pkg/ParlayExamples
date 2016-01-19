import parlay

@parlay.local_endpoint(auto_connect=True)
class Adder(parlay.ParlayCommandEndpoint):

    @parlay.parlay_command()
    def echo(self, text):
        print text

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