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
    distanceX = x - rover.x
    distanceY = y - rover.y
    heading = math.atan(distanceY/distanceX)
    heading = heading * (180/(math.pi))
    if heading < 0:
        turn_right(rover, left_side_speed, right_side_speed)
    if heading > 0:
        turn_left(rover, left_side_speed, right_side_speed)
    if distanceX == 0 and distanceY == 0:
        print("DONE!!")
    
def main():
    rover = Rover()
    

