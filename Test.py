from qset_lib import Rover
from time import sleep
import rospy

def main():
    rover = Rover()

    i = 0
    Wall = 0

    left_side_speed = 5
    right_side_speed = 5

    while not rospy.is_shutdown():
        print("X: " + str(rover.x) + " Y: " + str(rover.y) + " Heading: " + str(rover.heading))
        print (rover.laser_distances)
        for dist in rover.laser_distances:
            if dist < 1.5:
                if left_side_speed == 5:
                    Wall = rover.heading
                left_side_speed = -1
                right_side_speed = 1
                rover.send_command(left_side_speed, right_side_speed)
            if rover.heading > Wall + 90:
                left_side_speed = 0
                right_side_speed = 0
                rover.send_command(left_side_speed, right_side_speed)
        sleep(0.05)


if __name__ == "__main__":
    main()
