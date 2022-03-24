from qset_lib import Rover
from time import sleep
import rospy
import math

rover = Rover()

def turn_left(rover, left_speed, right_speed):
    temp = rover.heading
    while(1):
        left_side_speed = -1
        right_side_speed = 1
        rover.send_command(left_side_speed, right_side_speed)
        # Here is where you would place the desired heading variable.
        if rover.heading > temp + 90:
            left_side_speed = 0
            right_side_speed = 0
            rover.send_command(left_side_speed, right_side_speed)
        break
        sleep(0.05)
        
def turn_right(rover, left_speed, right_speed):
  temp = rover.heading
  while(1):
      left_side_speed = 1
      right_side_speed = -1
      rover.send_command(left_side_speed, right_side_speed)
      # Here is where you would place the desired heading variable.
      if rover.heading < temp - 90:
          left_side_speed = 0
          right_side_speed = 0
          rover.send_command(left_side_speed, right_side_speed)
      break
  sleep(0.05)

def reset_heading(rover, left_side_speed, right_side_speed):
    temp = rover.heading
    for dist in laser_distances:
        if dist > 10:
            while(1):
                left_side_speed = 1
                right_side_speed = -1
                rover.send_command(left_side_speed, right_side_speed)
      # Here is where you would place the desired heading variable.
                if rover.heading = range(-1, 1):
                    left_side_speed = 0
                    right_side_speed = 0
                    rover.send_command(left_side_speed, right_side_speed)
                break
            sleep(0.05)
            
 def findHeading(rover, rover.heading, objective):

    #find the slope between the two points, x2-x1 on top to make it relative to the y-axis (0 degrees)

    m = (objective[0]-self.x)/(objective[1]-self.y)

    #take the arctan of the slope to find the heading angle

    return math.atan(m)           

  i = 0
  Wall = 0        


def main():
    
    
  
   
  

    
    while not rospy.is_shutdown():
        left_side_speed = 5
        right_side_speed = 5
        rover.send_command(left_side_speed, right_side_speed)
        
        
        print("X: " + str(rover.x) + " Y: " + str(rover.y) + " Heading: " + str(rover.heading))
        print (rover.laser_distances)
        for dist in rover.laser_distances:
               if dist < 5:
                turn_right(rover, left_side_speed, right_side_speed)
                reset_heading(rover, left_side_speed, right_side_speed)
#                if left_side_speed == 5:
#                    Wall = rover.heading
#                left_side_speed = -1
#                right_side_speed = 1
#                rover.send_command(left_side_speed, right_side_speed)
#            if rover.heading > Wall + 90:
#                left_side_speed = 0
#                right_side_speed = 0
#                rover.send_command(left_side_speed, right_side_speed)
    sleep(0.05)


if __name__ == "__main__":
    main()

    

