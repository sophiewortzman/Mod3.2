from qset_lib import Rover
from time import sleep

def main():
    rover = Rover()
    left_speed = 1
    right_speed = 1
    def send_command(self, left_speed, right_speed):
        msg = wheelSpeed()
        msg.left = left_speed
        msg.right = right_speed
        self.__cmd_pub.publish(msg)
