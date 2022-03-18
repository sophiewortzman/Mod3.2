from qset_lib import Rover
from time import sleep

def main():
    rover = Rover()
    left_speed = 1
    right_speed = 1
    rover.send_command(left_speed, right_speed)
