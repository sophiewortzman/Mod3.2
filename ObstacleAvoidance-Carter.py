from qset_lib import Rover
from time import sleep
import rospy
from wheel_control import wheelSpeed

#find out how to use data from lidar array
from sensor_msgs import LaserScan
laser = LaserListener()
def __init__(self):
    self.laserSub = rospy.Subscriber("/leddar/leddarData", LaserScan, self.laser_callback, queue_size=1)
    self.laserRanges = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
def laser_callback(self, msg):
    self.laserRanges = msg.ranges

    
def main():
    rover = Rover()
    

