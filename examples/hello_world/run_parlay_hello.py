from parlay import start, local_item, parlay_command, ParlayCommandItem, ParlayProperty


@local_item(auto_connect=True)
class CheerfulPerson(ParlayCommandItem):

    hello_string = ParlayProperty(default="Hello World!", val_type=str)

    @parlay_command()
    def say_hello(self):
        return self.hello_string


if __name__ == "__main__":
    # this function call starts Parlay, and does not return
    start()
