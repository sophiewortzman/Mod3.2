from qset_lib import Rover
from time import sleep

def main():
    rover = Rover()

    i = 0

    left_side_speed = 5
    right_side_speed = 5

    while i < 3000:
        #print("X: " + rover.x + " Y: " + rover.y + " Heading: " + rover.heading)
        #from sensor_msgs.msg import LaserScan
        for dist in rover.laser_distances:
            if dist < 1.5:
                left_side_speed = 0
                right_side_speed = 0
                rover.send_command(left_side_speed, right_side_speed)
        rover.send_command(left_side_speed, right_side_speed)
        i = i + 1
        sleep(0.01)


if __name__ == "__main__":
    main()
