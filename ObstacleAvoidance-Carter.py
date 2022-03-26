from qset_lib import Rover
from time import sleep
import rospy
from wheel_control import wheelSpeed

#find out how to use data from lidar array
from sensor_msgs import LaserScan
laser = LaserListener()
#HARD CODE COORDINATES
x=
y=
def get_heading(x,y):
    distanceX = x -rover.x
    distanceY = y - rover.y
    heading = math.arctan(distanceY/distanceX)
    
    

    
def main():
    rover = Rover()
    

