#!/usr/bin/python

import rospy
from qset_msgs.msg import sabertooth
from std_msgs.msg import Float64

arm_sabertooth_addrs = [
    {"address": 129, "command": 6, "joint": "pan", "multi": 64},
    {"address": 129, "command": 7, "joint":  "shoulder", "multi": 64},
    {"address": 128, "command": 7, "joint": "elbow", "multi": 64},
    {"address": 130, "command": 6, "joint": "wrist_pitch", "multi": 64}
]

class ArmSabertoothController:

    def __init__(self):
        rospy.init_node("gazebo_arm_sabertooth")

        cmd_sub = rospy.Subscriber("/arm/sabertooth", sabertooth, self.sabertoothCallback, queue_size=1)
        self.pubs = {
            "pan": rospy.Publisher("/pan_joint_controller/command", Float64, queue_size=1),
            "shoulder": rospy.Publisher("/shoulder_joint_controller/command", Float64, queue_size=1),
            "elbow": rospy.Publisher("/linear_actuator_force", Float64, queue_size=1),
            "wrist_pitch":  rospy.Publisher("/wrist_pitch_joint_controller/command", Float64, queue_size=1)
        }

        rospy.spin()

    def sabertoothCallback(self, msg):
        motor = None
        multiplier = 1
        for addr in arm_sabertooth_addrs:
            if addr["address"] == msg.address and addr["command"] == msg.command:
                motor = addr["[joint]"]
                multiplier = addr["multi"]

        if motor is not None:
            outMsg = Float64()
            outMsg.data = self.getSpeedFromSabertoothSpeed(msg.data, multiplier)
            self.pubs[motor].publish(outMsg)

    def getSpeedFromSabertoothSpeed(self, data, multiplier):
        speed = (data - 64) / multiplier
        return speed


if __name__ == '__main__':
    driveController = ArmSabertoothController()
