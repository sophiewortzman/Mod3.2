#Mathew's LiDAR Code
# Matt's Lidar Branch

# Given by client:

# start of laser scan code
from sensor_msgs.msg import LaserScan


class LaserListener:

    def __init__(self):
        self.laserSub = rospy.Subscriber("/leddar/leddarData", LaserScan, self.laser_callback, queue_size=1)
        self.laserRanges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def laser_callback(self, msg):
        # type: (LaserScan) -> None
        self.laserRanges = msg.ranges


# end of laser scan code access laserRanges for an array of all measured distances from the laser sensors

print(laserRanges)


# Things that might be helpful:

# import lidar library
import ydlidar

# allows the lidar to be referred to as laser
laser = ydlidar.CYdLidar()

# possible lidar properties
laser.setlidaropt(ydlidar.LidarPropSerialPort, port)
laser.setlidaropt(ydlidar.LidarPropSerialBaudrate, 512000)
laser.setlidaropt(ydlidar.LidarPropLidarType, ydlidar.TYPE_TOF)
laser.setlidaropt(ydlidar.LidarPropDeviceType, ydlidar.YDLIDAR_TYPE_SERIAL)
laser.setlidaropt(ydlidar.LidarPropScanFrequency, 10.0)
laser.setlidaropt(ydlidar.LidarPropSampleRate, 20)
laser.setlidaropt(ydlidar.LidarPropSingleChannel, False)

# makes sure lidar works
r = laser.doProcessSimple(scan)
if r:
    print("Scan received[", scan.stamp, "]:", scan.points.size(), "ranges is [", 1.0 / scan.config.scan_time, "]Hz")
else:
    print("Failed to get Lidar Data.")
