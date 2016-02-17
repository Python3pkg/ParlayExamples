from parlay import start, local_item, ParlayCommandItem, parlay_command
from parlay.utils import sleep


@local_item(auto_connect=True)
class Item1(ParlayCommandItem):

    @parlay_command()
    def slow_command_1(self):
        sleep(5)
        return "Command 1 Completed!"

    @parlay_command()
    def delete_me(self):
        return "Boo!"


@local_item(auto_connect=True)
class Item2(ParlayCommandItem):

    @parlay_command()
    def slow_command_2(self):
        sleep(5)
        return "Command 2 Completed!"

    @parlay_command()
    def delete_me(self):
        return "Boo!"


if __name__ == "__main__":
    start(open_browser=False)  # you can avoid launching your web browser

