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
            if dist < 1.5:
                if left_side_speed == 5:
                    Wall = rover.heading
                left_side_speed = -1
                right_side_speed = 1
                rover.send_command(left_side_speed, right_side_speed)      
            if rover.heading > Wall + 80:
                left_side_speed = 3
                right_side_speed = 3
                rover.send_command(left_side_speed, right_side_speed)
                
                if dist > 5:
                    sleep(0.1)
                    left_side_speed = 1
                    right_side_speed = -1
                    rover.send_command(left_side_speed, right_side_speed)
                    print("left_side_speed: " + str(left_side_speed) + " right_side_speed: " + str(right_side_speed))

            if rover.heading < Wall - 1:
                left_side_speed = 5
                right_side_speed = 5
                rover.send_command(left_side_speed, right_side_speed)
            
        sleep(0.05)


if __name__ == "__main__":
    main()
