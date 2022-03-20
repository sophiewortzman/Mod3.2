from qset_lib import Rover
from time import sleep
import rospy

def main():
    rover = Rover()

    i = 0
    Wall = 0

    left_side_speed = 5
    right_side_speed = 5
    rover.send_command(left_side_speed, right_side_speed)

    while not rospy.is_shutdown():
        print("X: " + str(rover.x) + " Y: " + str(rover.y) + " Heading: " + str(rover.heading))
        print (rover.laser_distances)
        
        for dist in rover.laser_distances:
            left_side_speed = 5
            right_side_speed = 5
            rover.send_command(left_side_speed, right_side_speed)
            
            if dist < 1.5:
                left_side_speed = -2
                right_side_speed = 2
                rover.send_command(left_side_speed, right_side_speed) 
                sleep(2.5)
                left_side_speed = 2
                right_side_speed = -2
                rover.send_command(left_side_speed, right_side_speed)
                sleep(2.5)
       
        sleep(0.05)


if __name__ == "__main__":
    main()
