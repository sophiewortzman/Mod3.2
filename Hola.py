from qset_lib import Rover
from time import sleep
import rospy


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


  for dist in rover.laser_distances:
        if dist > 5:
            while(1):
                left_side_speed = 1
                right_side_speed = -1
                rover.send_command(left_side_speed, right_side_speed)
      # Here is where you would place the desired heading variable.

            

  i = 0
  Wall = 0        


def main():
    while (1):
        x=0
        while (x < (len(rover.laser_distances)+1)):
            rover.laser_distances[x] = distances[x]
            x = x+1
    
    
  
   
  

    
    while not rospy.is_shutdown():
        left_side_speed = 5
        right_side_speed = 5
        rover.send_command(left_side_speed, right_side_speed)
        
        
        print("X: " + str(rover.x) + " Y: " + str(rover.y) + " Heading: " + str(rover.heading))
        print distances[1]
       
        for dist in rover.laser_distances:
               if dist < 5:
                turn_right(rover, left_side_speed, right_side_speed)
                reset_heading(rover, left_side_speed, right_side_speed)

    sleep(0.05)


if __name__ == "__main__":
    main()
