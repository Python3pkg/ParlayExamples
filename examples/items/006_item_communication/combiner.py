import parlay


@parlay.local_item(auto_connect=True)
class Combiner(parlay.ParlayCommandItem):

    @parlay.parlay_command()
    def echo(self, text):
        print text

    @parlay.parlay_command()
    def add_products(self, x, y):
        """
        Will add x and y and then return and echo the result

        ###Parlay will perform automatic type coercian if possible if the type is specified###

        :type x int
        :type y int
        """
        adder = self.get_item_by_name("Adder")
        multiplier = self.get_item_by_name("Multiplier")
        result = adder.add(x, y) + multiplier.multiply(x,y)
        self.echo(result)

        return result

    @parlay.parlay_command(async=True)
    def foo(self, x, y):
        return x+y

    @parlay.parlay_command()
    def bar(self, a, b):
        return self.foo(a,b)
