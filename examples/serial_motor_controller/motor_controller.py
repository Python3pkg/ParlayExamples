from parlay.protocols.serial_line import ASCIILineProtocol, LineItem
from parlay import parlay_command, start


class SerialMotorControllerProtocol(ASCIILineProtocol):

    def __init__(self, port):
        ASCIILineProtocol.__init__(self, port=port)
        self.items = [SerialMotorControllerItem(1, "Motor1", "Motor1", self),
                      SerialMotorControllerItem(2, "Motor2", "Motor2", self)]

    @classmethod
    def open(cls, broker, port="/dev/ttyUSB0"):
        return super(SerialMotorControllerProtocol, cls).open(broker, port=port, baudrate=115200, delimiter="\r")


class SerialMotorControllerItem(LineItem):

    def __init__(self, motor_index, item_id, name, protocol):
        LineItem.__init__(self, item_id, name, protocol)
        self._motor_index = motor_index

    @parlay_command()
    def spin(self, speed):
        """
        Move the motor at a constant speed, between -9 and 9.  Negative speed causes motor to spin in reverse.
        :param speed: speed to move
        :type speed int
        :return: none
        """
        speed = int(speed)
        if speed > 9 or speed < -9:
            raise ValueError("Speed outside range")
        direction = "f" if speed >= 0 else "r"
        self.send_raw_data("{}{}{}".format(self._motor_index, direction, abs(speed)))
        return self.wait_for_data()

    @parlay_command()
    def stop(self):
        """
        Stop the motor
        :return: none
        """
        return self.spin(0)


if __name__ == "__main__":

    start()
