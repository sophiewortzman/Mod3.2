import rospy
from qset_msgs.msg import *
from gazebo_msgs.msg import ModelStates, ModelState
from geometry_msgs.msg import Quaternion, Twist
from qset_msgs.msg import wheelSpeed
from sensor_msgs.msg import LaserScan
import math
from tf.transformations import euler_from_quaternion

class Rover:
    def __init__(self):
        rospy.init_node("mod3_lib")
        self.x = 0.0
        self.y = 0.0
        self.heading = 0.0
        self.__name = "robot"
        ms_sub = rospy.Subscriber("/gazebo/model_states", ModelStates, self.__modelstates_callback, queue_size=1)
        laser_sub = rospy.Subscriber("/scan", LaserScan, self.__laser_callback, queue_size=1)
        self.__cmd_pub = rospy.Publisher("/wheelSpeedTopic", wheelSpeed, queue_size=1)
        self.laser_distances = []


    def __modelstates_callback(self, msg):
        for name, pose in zip(msg.name, msg.pose):
            if name == self.__name:
                self.x = pose.position.x
                self.y = pose.position.y

                self.heading = euler_from_quaternion([pose.orientation.x, pose.orientation.y, pose.orientation.z,
                                                      pose.orientation.w])[2] / math.pi * 180.0


    def send_command(self, left_speed, right_speed):
        msg = wheelSpeed()
        msg.left = left_speed
        msg.right = right_speed
        self.__cmd_pub.publish(msg)

    def __laser_callback(self, msg):
        self.laser_distances = msg.ranges
