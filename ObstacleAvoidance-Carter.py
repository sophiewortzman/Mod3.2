#Carter's Code for implemeneting obstacle avoidance
from qset_lib import Rover
from time import sleep
import rospy

def main():
  distances = []
  rover=Rover()
  while (1):
    distances = rover.laser_distances.copy()
    print (distances(1))
  
  
