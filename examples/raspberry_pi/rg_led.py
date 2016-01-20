#!/usr/bin/env python
import parlay
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location



@parlay.local_item(auto_connect=True)
class RG_LED(parlay.ParlayCommandItem):

    R_PIN = parlay.parlay_property(val_type=int, default=11)
    G_PIN = parlay.parlay_property(val_type=int, default=12)

    @parlay.parlay_command()
    def init(self):

        GPIO.setup(self.R_PIN, GPIO.OUT)
        GPIO.output(self.R_PIN, GPIO.HIGH)

        GPIO.setup(self.G_PIN, GPIO.OUT)
        GPIO.output(self.G_PIN, GPIO.HIGH)

        self.p_R = GPIO.PWM(self.R_PIN, 2000)  # set Frequency to 2KHz
        self.p_G = GPIO.PWM(self.G_PIN, 2000)

        self.p_R.start(0)      # Initial duty Cycle = 0(leds off)
        self.p_G.start(0)

    @parlay.parlay_command()
    def turn_green(self):
        self.p_R.ChangeDutyCycle(0)
        self.p_G.ChangeDutyCycle(100)

    @parlay.parlay_command()
    def turn_red(self):
        self.p_G.ChangeDutyCycle(0)
        self.p_R.ChangeDutyCycle(100)

    @parlay.parlay_command()
    def turn_off(self):
        self.p_G.ChangeDutyCycle(0)
        self.p_R.ChangeDutyCycle(0)

if __name__ == "__main__":
    parlay.start()
