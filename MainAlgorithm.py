from qset_lib import Rover
from time import sleep

#import lidar data
from sensor_msgs.msg import LaserScan


class LaserListener:

    def __init__(self):
        self.laserSub = rospy.Subscriber("/leddar/leddarData", LaserScan, self.laser_callback, queue_size=1)
        self.laserRanges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# end of laser scan code access laserRanges for an array of all measured distances from the laser sensors

def main():
    
     def laser_callback(self, msg):
        # type: (LaserScan) -> None
        self.laserRanges = msg.ranges
    rover = Rover()

    i = 0

    left_side_speed = 1
    right_side_speed = 1

    while i < 1000:
        print("X: " + rover.x + " Y: " + rover.y + " Heading: " + rover.heading)
        for dist in rover.laser_distances:
            if dist < 0.1:
                print("TOO CLOSE")
                left_side_speed = 0
                right_side_speed = 0     
        rover.send_command(left_side_speed, right_side_speed)
        i = i + 1
        sleep(0.01)

        #run dijkstra's algorithm
        #import Dijkstra
         
         #turn left
         

if __name__ == "__main__":
    main()
