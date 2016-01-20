#!/usr/bin/env python
import parlay
import LCD1602
import time


@parlay.local_item(auto_connect=True)
class LCD(parlay.ParlayCommandItem):

    TEXT = parlay.parlay_property(val_type=str, default="Hello World")

    @parlay.parlay_command()
    def init(self):

        LCD1602.init(0x27, 1)   # init(slave address, background light)
        LCD1602.write(0, 0, 'Hello')
        LCD1602.write(1, 1, 'World')
        time.sleep(1)
        LCD1602.clear()

    @parlay.parlay_command()
    def loop(self):
        current_text = ""
        while True:
            "Scroll Text"
            # add whitespace
            if len(self.TEXT) > 16:
                text = self.TEXT
                # fancy scrolling if we have a long string
                for i in range(len(text)):
                    #break if text changes
                    if text != self.TEXT:
                        break
                    LCD1602.write(0, 0, text)
                    text = text[1:]
                    time.sleep(0.5)
                    LCD1602.clear()
            elif current_text != self.TEXT:
                #static change
                LCD1602.clear()
                LCD1602.write(0, 0, self.TEXT)
                current_text = self.TEXT
                time.sleep(1) # hold for at least 1 second
            else:  # sleep poll
                time.sleep(1)





if __name__ == "__main__":
    parlay.start()