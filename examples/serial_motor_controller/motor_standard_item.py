from parlay.protocols.serial_line import ASCIILineProtocol
from parlay.items.parlay_standard import ParlayStandardItem
from parlay.items.base import INPUT_TYPES, MSG_TYPES, MSG_STATUS
from parlay import start


class SerialMotorControllerProtocol(ASCIILineProtocol):

    def __init__(self, port):
        ASCIILineProtocol.__init__(self, port=port)
        self.items = [SerialMotorControllerItem(1, "Motor1", "Motor 1", self),
                      SerialMotorControllerItem(2, "Motor2", "Motor 2", self)]

    @classmethod
    def open(cls, broker, port="/dev/ttyUSB0"):
        return super(SerialMotorControllerProtocol, cls).open(broker, port=port, baudrate=115200, delimiter="\r")


class SerialMotorControllerItem(ParlayStandardItem):
    """
    This examples implements SerialMotorControllerItem as an extension of ParlayStandardItem.

    This is NOT the easiest way to do this!   ParlayCommandItem offers several abstractions
    that make this much easier.

    However, if you have a use case where you must build your own discovery information, and handle
    raw Parlay messages, this example shows how to do it.
    """

    def __init__(self, motor_index, item_id, name, protocol):
        self._motor_index = motor_index
        self._protocol = protocol

        ParlayStandardItem.__init__(self, item_id, name)

        # manually add command options
        dropdown_options = [("spin", "spin")]
        dropdown_sub_fields = [[self.create_field("speed", INPUT_TYPES.NUMBER,
                                                  label="speed to spin (-9 to 9)", required=True)]]

        dropdown_options.append(("stop", "stop"))
        dropdown_sub_fields.append([])

        self.add_field("COMMAND",
                       INPUT_TYPES.DROPDOWN,
                       dropdown_options=dropdown_options,
                       dropdown_sub_fields=dropdown_sub_fields)

    def on_message(self, msg):
        if "COMMAND" in msg["CONTENTS"]:

            cmd = msg["CONTENTS"]["COMMAND"]
            resp_to = msg["TOPICS"]["FROM"]

            if cmd == "spin":
                try:
                    result = self.spin(msg["CONTENTS"]["speed"])
                    contents = {"RESULT": result}
                    msg_status = MSG_STATUS.OK
                except Exception as e:
                    contents = {"DESCRIPTION": e.message, "ERROR": e.message}
                    msg_status = MSG_STATUS.ERROR
                self.send_message(to=resp_to, msg_type=MSG_TYPES.RESPONSE, msg_status=msg_status, contents=contents)

            elif cmd == "stop":
                try:
                    result = self.stop()
                    contents = {"RESULT": result}
                    msg_status = MSG_STATUS.OK
                except Exception as e:
                    contents = {"DESCRIPTION": e.message, "ERROR": e.message}
                    msg_status = MSG_STATUS.ERROR
                self.send_message(to=resp_to, msg_type=MSG_TYPES.RESPONSE, msg_status=msg_status, contents=contents)

            else:
                self.send_message(to=resp_to, msg_type=MSG_TYPES.RESPONSE, msg_status=MSG_STATUS.ERROR,
                                  contents={"DESCRIPTION": "Unsupported command {}".format(cmd)})

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
        data = "{}{}{}".format(self._motor_index, direction, abs(speed))

        self._protocol.sendLine(data)

    def stop(self):
        """
        Stop the motor
        :return: none
        """
        return self.spin(0)


if __name__ == "__main__":

    start()
