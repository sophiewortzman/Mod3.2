#!/usr/bin/python

import rospy
from qset_msgs.msg import sabertooth
from std_msgs.msg import Float64

wheel_sabertooth_addrs = [
    {"address": 128, "command": 7, "wheel": "front_right", "multi": 10.},
    {"address": 130, "command": 6, "wheel":  "front_left", "multi": 10.},
    {"address": 130, "command": 7, "wheel": "back_right", "multi": 10.},
    {"address": 128, "command": 6, "wheel": "back_left", "multi": 10.}
]


class WheelSabertoothController:

    def __init__(self):
        rospy.init_node("gazebo_wheels_sabertooth")

        cmd_sub = rospy.Subscriber("/wheels/sabertooth", sabertooth, self.sabertoothCallback, queue_size=1)
        self.pubs = {
            "back_left": rospy.Publisher("/back_left_wheel_joint_controller/command", Float64, queue_size=1),
            "back_right": rospy.Publisher("/back_right_wheel_joint_controller/command", Float64, queue_size=1),
            "front_left":  rospy.Publisher("/front_left_wheel_joint_controller/command", Float64, queue_size=1),
            "front_right": rospy.Publisher("/front_right_wheel_joint_controller/command", Float64, queue_size=1)
        }

        rospy.spin()

    def sabertoothCallback(self, msg):
        motor = None
        multiplier = 1
        for addr in wheel_sabertooth_addrs:
            if addr["address"] == msg.address and addr["command"] == msg.command:
                motor = addr["wheel"]
                multiplier = addr["multi"]

        if motor is not None:
            outMsg = Float64()
            outMsg.data = self.getSpeedFromSabertoothSpeed(msg.data, multiplier)
            self.pubs[motor].publish(outMsg)

    def getSpeedFromSabertoothSpeed(self, data, multiplier):
        speed = (data - 64.) / multiplier
        rospy.loginfo("Got data: " + str(data) + " output: " + str(speed))
        return speed


if __name__ == '__main__':
    driveController = WheelSabertoothController()
