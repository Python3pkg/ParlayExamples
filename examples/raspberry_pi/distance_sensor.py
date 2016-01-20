#!/usr/bin/env python
import parlay
import RPi.GPIO as GPIO
import time

@parlay.local_item(auto_connect=True)
class DISTANCE_SENSOR(parlay.ParlayCommandItem):

    TRIG_PIN = parlay.parlay_property(val_type=int, default=13)
    ECHO_PIN = parlay.parlay_property(val_type=int, default=15)

    DISTANCE = parlay.parlay_datastream(default=0)
    POLLING = parlay.parlay_property(val_type=int, default=0)
    POLLING_INTERVAL = parlay.parlay_property(val_type=int, default=1)

    @parlay.parlay_command()
    def init(self):
        GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location

        GPIO.setup(self.TRIG_PIN, GPIO.OUT)
        GPIO.setup(self.ECHO_PIN, GPIO.IN)


    @parlay.parlay_command()
    def poll(self):
        GPIO.output(self.TRIG_PIN, 0)
        time.sleep(0.000002)  # let it settle

        GPIO.output(self.TRIG_PIN, 1)
        time.sleep(0.00001)  # let it settle
        GPIO.output(self.TRIG_PIN, 0)

        #busy loop. wait for echo pin to go high
        while GPIO.input(self.ECHO_PIN) == 0:
            pass
        time1 = time.time()
        while GPIO.input(self.ECHO_PIN) == 1:
            pass
        time2 = time.time()

        duration = time2 - time1
        self.DISTANCE = duration * 340 / 2 * 100
        return self.DISTANCE

    @parlay.parlay_command()
    def poll_forever(self):
        while True:
            self.poll()
            time.sleep(self.POLLING_INTERVAL)


if __name__ == "__main__":
    parlay.start()