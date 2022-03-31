from qset_lib import Rover
from time import sleep
import rospy
import math
rover = Rover()
rover.laser_distances = [0] * 30
sum1 = 0
sum2 = 0
objectivex = 10
objectivey = 10

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
        sleep(0.3)
        
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
  sleep(0.3)

#call this to find the new heading angle after the rover turns (returns heading angle)
def find_heading(rover, objectivex, objectivey):

    #find the slope between the two points relative top the x-axis (0 degrees)
    m = (objectivey-rover.y)/(objectivex-rover.x)

    #take the arctan of the slope to find the heading angle
    #if rover.y < objectivey:
    return math.atan(m) * 180 / math.pi * (-1)
    #else:
        #return math.atan(m) * 180 / math.pi 

def reset_heading(rover, left_side_speed, right_side_speed, find_heading):
   
            
            
            
            tempHeading = find_heading(rover, objectivex, objectivey)
            
          
            
            if (tempHeading-2<=rover.heading<=tempHeading+2):
                #if rover.heading == range(lowerBound, upperBound):
                left_side_speed = 2
                right_side_speed = 2
                rover.send_command(left_side_speed, right_side_speed)
            
            if (tempHeading-2>=rover.heading) or (rover.heading>=tempHeading+2):
                left_side_speed = 1
                right_side_speed = -1
                rover.send_command(left_side_speed, right_side_speed)
               
                
             
            
            
            

           
                
            
           
                
      # Here is where you would place the desired heading variable.
            
        
            
#call this before obstacle avoidance to find which way is the best to turn (returns "left" or "right")
def side_to_favour():
    
    sumRight = 0
    sumLeft = 0
    count = 0

    while(count <= 29):

        if count <= 15:
            if rover.laser_distances[count] != float('inf'):
                sumRight += rover.laser_distances[count]
                print("value:", rover.laser_distances[count])

            else:
                print("ADDING 200")
                sumRight += 200
        
        if count >= 15:

            if rover.laser_distances[count] != float('inf'):
                sumLeft += rover.laser_distances[count]
                print("value:", rover.laser_distances[count])

            else:
                print("Adding 200")
                sumLeft += 200

        count += 1
        print(count)
    print("sumLeft:", sumLeft)
    print("sumRight:", sumRight)

    if sumLeft > sumRight:
        return "left"
            

    if sumRight > sumLeft:
        return "right"

    if sumRight == sumLeft:
        print("equal")

    else:
        return "NOT WORKING"       

def main():  
    
  
    while not rospy.is_shutdown():
        
        if (rover.x == objectivex) and (rover.y == objectivey):
            left_side_speed = 0 
            right_side_speed = 0
            rover.send_command(left_side_speed, right_side_speed)
        
        left_side_speed = 2 
        right_side_speed = 2
        rover.send_command(left_side_speed, right_side_speed)
        
        
        print("X: " + str(rover.x) + " Y: " + str(rover.y) + " Heading: " + str(rover.heading))
        print (rover.laser_distances)

        for dist in rover.laser_distances:
                      
            if dist < 2:
                
                whichWay = side_to_favour()
                #print(whichWay)

                if whichWay == "right":
                    print(whichWay)
                    turn_right(rover, left_side_speed, right_side_speed)
                       
                        
                if whichWay == "left":
                    print(whichWay)
                    turn_left(rover, left_side_speed, right_side_speed)

            if dist > 5:
                
                reset_heading(rover, left_side_speed, right_side_speed, find_heading)
                
           
            while ((objectivex - 0.5) < rover.x < (objectivex + 0.5)):
                while ((objectivey - 0.5) < rover.y < (objectivey + 0.5)):
                    left_side_speed = 0
                    right_side_speed = 0
                    rover.send_command(left_side_speed, right_side_speed)

                #tempHeading = find_heading(rover, objectivex, objectivey)
                #print(find_heading(rover, objectivex, objectivey))
                
                
                #if (tempHeading - 1 <= rover.heading <= tempHeading + 1):
                    #left_side_speed = 2
                    #right_side_speed = 2
                    #rover.send_command(left_side_speed, right_side_speed)
                
                #if (tempHeading - 1 >= rover.heading) or (rover.heading >= tempHeading + 1):
                    #reset_heading(rover, left_side_speed, right_side_speed, find_heading)
                                    
                #break
                
        sleep(0.05)

if __name__ == "__main__":
    main()
