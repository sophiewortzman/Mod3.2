#Carter's Code for implemeneting obstacle avoidance
from qset_lib import Rover
from time import sleep
import rospy

def main():
  distances = []
  rover=Rover()
  while (1):
    print(rover.laser_distances(1))  
  
