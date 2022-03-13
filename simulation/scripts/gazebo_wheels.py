#!/usr/bin/python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Float32
from std_msgs.msg import Float64
from qset_msgs.msg import perWheelSpeed
from qset_msgs.msg import wheelSpeed
import math

half_distance_between_wheels = 0.6


class DriveController:

    def __init__(self):
        rospy.init_node("gazebo_wheels")

        # self.cmd_pub = rospy.Publisher("/diff_drive_controller/cmd_vel", Twist, queue_size=1)
        cmd_sub = rospy.Subscriber("/cmd_vel", Twist, self.inCallBack, queue_size=1)
        self.bl_pub = rospy.Publisher("/back_left_wheel_joint_controller/command", Float64, queue_size=1)
        self.br_pub = rospy.Publisher("/back_right_wheel_joint_controller/command", Float64, queue_size=1)
        self.fl_pub = rospy.Publisher("/front_left_wheel_joint_controller/command", Float64, queue_size=1)
        self.fr_pub = rospy.Publisher("/front_right_wheel_joint_controller/command", Float64, queue_size=1)
        ws_sub = rospy.Subscriber("/wheelSpeedTopic", wheelSpeed, self.wheelControlCallBack, queue_size=1)
        pws_sub = rospy.Subscriber("wheel/speeds", perWheelSpeed, self.perWheelSpeedCallBack, queue_size=1)
#        plan_sub =rospy.Subscriber("/move_base/TrajectoryPlannerROS/local_plan", Path, self.pathCallback, queue_size=1)
#        self.heading_pub = rospy.Publisher("/desired_heading", Float32, queue_size=1)

        rospy.spin()

    def wheelControlCallBack(self, msg):
        temp = Float64()
        temp.data = msg.left
        self.bl_pub.publish(temp)
        self.fl_pub.publish(temp)
        temp.data = msg.right
        self.fr_pub.publish(temp)
        self.br_pub.publish(temp)

    def perWheelSpeedCallBack(self, msg):
        msg = perWheelSpeed()
        temp = Float64()
        temp.data = msg.backLeft
        self.bl_pub.publish(temp)
        temp.data = msg.frontLeft
        self.fl_pub.publish(temp)
        temp.data = msg.backRight
        self.br_pub.publish(temp)
        temp.data = msg.frontRight
        self.fr_pub.publish(temp)

    def inCallBack(self, msg):
        wheelSpeedMsg = wheelSpeed()
        if msg.angular.z != 0.0:
            R = msg.linear.x / msg.angular.z
            wheelSpeedMsg.right = (msg.angular.z * (R + half_distance_between_wheels)) + msg.linear.x
            wheelSpeedMsg.left = (msg.angular.z * (R - half_distance_between_wheels)) + msg.linear.x
        else:
            wheelSpeedMsg.right = msg.linear.x * 10
            wheelSpeedMsg.left = msg.linear.x * 10

        self.wheelControlCallBack(wheelSpeedMsg)

    def pathCallback(self, msg):
        first = msg.poses[0]
        last = msg.poses[len(msg.poses) -1]
        heading = math.atan((first.pose.position.x - last.pose.position.x) / (first.pose.position.y - last.pose.position.y)) if (first.pose.position.y - last.pose.position.y) != 0 else math.pi / 2.0
        out = Float32()
        out.data = heading
        print ("Heading: %f   Len: %d", heading * 180.0 / math.pi, len(msg.poses))
        self.heading_pub.publish(out)


if __name__ == '__main__':
    driveController = DriveController()
