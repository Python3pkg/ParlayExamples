from parlay.protocols.serial_line import ASCIILineProtocol, LineEndpoint
from parlay import parlay_command, start


class SerialMotorControllerProtocol(ASCIILineProtocol):

    def __init__(self, port):
        ASCIILineProtocol.__init__(self, port=port)
        self.endpoints = [SerialMotorControllerItem(1, "Motor1", "Motor1", self),
                          SerialMotorControllerItem(2, "Motor2", "Motor2", self)]

    @classmethod
    def open(cls, broker, port="/dev/ttyUSB0"):
        return super(SerialMotorControllerProtocol, cls).open(broker, port=port, baudrate=115200, delimiter="\r")


class SerialMotorControllerItem(LineEndpoint):

    def __init__(self, motor_index, endpoint_id, name, protocol):
        LineEndpoint.__init__(self, endpoint_id, name, protocol)
        self._motor_index = motor_index
        self._protocol = protocol

    @parlay_command()
    def move_at_velocity(self, velocity):
        """
        Move the motor at a constant velocity, between -10 and 10.
        Negative velocity causes motor to spin in reverse.
        :param velocity: speed to move
        :type velocity int
        :return: none
        """
        if velocity > 10 or velocity < -10:
            raise ValueError("Velocity outside range")
        velocity = int(velocity)
        direction = "f" if velocity >= 0 else "r"
        self.send_raw_data("{}{}{}".format(self._motor_index, direction, velocity))
        return self.wait_for_data()

    @parlay_command()
    def stop(self):
        """
        Stop the motor
        :return: none
        """
        return self.move_at_velocity(0)


if __name__ == "__main__":

    start()
