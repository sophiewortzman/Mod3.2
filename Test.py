from qset_lib import Rover
from time import sleep

def main():
    rover = Rover()
    left_side_speed = 1
    right_side_speed = 1
    rover.send_command(left_side_speed, right_side_speed)
