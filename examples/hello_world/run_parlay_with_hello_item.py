from parlay import start, local_item, parlay_command, ParlayCommandItem


@local_item(auto_connect=True)
class CheerfulPerson(ParlayCommandItem):

    @parlay_command()
    def say_hello(self):
        return "Hello World!"


if __name__ == "__main__":
    # this function call starts Parlay, and does not return
    start()
