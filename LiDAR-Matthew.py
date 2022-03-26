from qset_lib import Rover
from time import sleep
import rospy
import math
rover = Rover()
rover.laser_distances = [0] * 30
sum1 = 0
sum2 = 0

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
        #print("Speed: " + left_side_speed)
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
                if rover.heading == range(-1, 1):
                    left_side_speed = 0
                    right_side_speed = 0
                    rover.send_command(left_side_speed, right_side_speed)
                break
            sleep(0.05)
  
#call this to find the new heading angle after the rover turns (returns heading angle)
def find_heading(rover, heading, objective):

    #find the slope between the two points, x2-x1 on top to make it relative to the y-axis (0 degrees)
    m = (objective[0]-self.x)/(objective[1]-self.y)

    #take the arctan of the slope to find the heading angle
    return math.atan(m) * 180 / math.pi  

#call this before obstacle avoidance to find which way is the best to turn (returns "left" or "right")
def side_to_favour():
    
    sumRight = 0
    sumLeft = 0
    count = 0

    while(count <= 29):

        if count <= 15:

            if rover.laser_distances[count] == "inf":
                sumRight += 200
                continue
            sumRight += rover.laser_distances[count]

        if count >= 15:

            if rover.laser_distances[count] == "inf":
                sumLeft += 200
                continue
            sumLeft += rover.laser_distances[count]
                
        count += 1

    if sumLeft > sumRight:
        return "left"
            

    if sumRight > sumLeft:
        return "right"

    else:
        return "NOT WORKING"
            
               
Wall = 0        


def main():  
    
  
    while not rospy.is_shutdown():
        left_side_speed = 5
        right_side_speed = 5
        rover.send_command(left_side_speed, right_side_speed)
        
        
        print("X: " + str(rover.x) + " Y: " + str(rover.y) + " Heading: " + str(rover.heading))
        print (rover.laser_distances)

        for dist in rover.laser_distances:
               if dist < 2:
                
                whichWay = side_to_favour()
                print(whichWay)
                if whichWay == "right":
                    print(whichWay)
                    turn_right(rover, left_side_speed, right_side_speed)
                    sleep(0.05)    
                        
                if whichWay == "left":
                    print(whichWay)
                    turn_left(rover, left_side_speed, right_side_speed)
                    sleep(0.05)
                else:
                    #print("NOT WORKING")
                    sleep(0.05)                

#                if left_side_speed == 5:
#                    Wall = rover.heading
#                left_side_speed = -1
#                right_side_speed = 1
#                rover.send_command(left_side_speed, right_side_speed)
#            if rover.heading > Wall + 90:
#                left_side_speed = 0
#                right_side_speed = 0
#                rover.send_command(left_side_speed, right_side_speed)
        


if __name__ == "__main__":
    main()

