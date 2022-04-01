from qset_lib import Rover
from time import sleep
import rospy
import math
rover = Rover()
rover.laser_distances = [0] * 30
sum1 = 0
sum2 = 0
objectivex = 15 #x is the red in gazebo
objectivey = 1 #y is green in gazebo

def turn_left(rover, left_speed, right_speed):
    
    while(1):
        left_side_speed = 0
        right_side_speed = 3
        rover.send_command(left_side_speed, right_side_speed)
        sleep(0.4)
        #print("Speed: " + left_side_speed)
        break
        
        
def turn_right(rover, left_speed, right_speed):
    
    while(1):
        left_side_speed = 3
        right_side_speed = 0
        rover.send_command(left_side_speed, right_side_speed)
        sleep(0.4)
        #print("Speed: " + right_side_speed)
        break
        

#call this to find the new heading angle after the rover turns (returns heading angle)
def find_heading(rover, objectivex, objectivey):

    m = (objectivey-rover.y)/(objectivex-rover.x) #find the slope between the two points relative top the x-axis (0 degrees)
    
    if(objectivey > 0) and (objectivex > 0): #Quadrant 1
        if (rover.y < objectivey) and (rover.x < objectivex): #1
            return (math.atan(m) * 180 / math.pi)
        if(rover.y > objectivey) and (rover.x > objectivex): #2
            return ((math.atan(m) * 180 / math.pi) - 180)
        if(rover.y > objectivey) and (rover.x < objectivex): #3
            return (math.atan(m) * 180 / math.pi)
        if(rover.y < objectivey) and (rover.x > objectivex): #4
            return ((math.atan(m) * 180 / math.pi) - 180)
    
    if(objectivey > 0) and (objectivex < 0): #Quadrant 2
        if(rover.y < objectivey) and (rover.x > objectivex): #1
            return ((math.atan(m) * 180 / math.pi) + 180)
        if(rover.y > objectivey) and (rover.x < objectivex): #2
            return (math.atan(m) * 180 / math.pi)
        if(rover.y > objectivey) and (rover.x > objectivex): #3
            return ((math.atan(m) * 180 / math.pi) - 180)
        if(rover.y < objectivey) and (rover.x < objectivex): #4
            return (math.atan(m) * 180 / math.pi)
        
    if(objectivey < 0) and (objectivex > 0): #Quadrant 3
        if(rover.y > objectivey) and (rover.x > objectivex): #1
            return ((math.atan(m) * 180 / math.pi) - 180)
        if(rover.y < objectivey) and (rover.x < objectivex): #2
            return (math.atan(m) * 180 / math.pi)
        if(rover.y > objectivey) and (rover.x < objectivex): #3
            return (math.atan(m) * 180 / math.pi)
        if(rover.y < objectivey) and (rover.x > objectivex): #4
            return ((math.atan(m) * 180 / math.pi) + 180)
    
    if(objectivey < 0) and (objectivex > 0): #Quadrant 4
        if(rover.y > objectivey) and (rover.x < objectivex): #1
            return (math.atan(m) * 180 / math.pi)
        if(rover.y < objectivey) and (rover.x > objectivex): #2
            return ((math.atan(m) * 180 / math.pi) + 180)
        if(rover.y < objectivey) and (rover.x < objectivex): #3
            return (math.atan(m) * 180 / math.pi)
        if(rover.y > objectivey) and (rover.x > objectivex): #4
            return ((math.atan(m) * 180 / math.pi) + 180)

    else:
        return

def reset_heading(rover, left_side_speed, right_side_speed, tempHeading):
    
            if (tempHeading+1>rover.heading>tempHeading-1):
                #if rover.heading == range(lowerBound, upperBound):
                left_side_speed = 4
                right_side_speed = 4
                rover.send_command(left_side_speed, right_side_speed)
                print("Destination is straight ahead...\n")
                sleep(0.1)
                return

            if (tempHeading>rover.heading>-179.99):
                left_side_speed = 0
                right_side_speed = 3
                rover.send_command(left_side_speed, right_side_speed)
                print("Turning left towards destination...\n")
                sleep(0.1)

            if (tempHeading<rover.heading<179.99):
                left_side_speed = 3
                right_side_speed = 0
                rover.send_command(left_side_speed, right_side_speed)
                print("Turning right towards destination...\n")
                sleep(0.1)
            
#call this before obstacle avoidance to find which way is the best to turn (returns "left" or "right")
def side_to_favour():
    sumRight = 0
    sumLeft = 0
    count = 0

    while(count <= 29):
        if count <= 15:
            if rover.laser_distances[count] != float('inf'):
                sumRight += rover.laser_distances[count]
                #print("value:", rover.laser_distances[count])
            else:
                #print("ADDING 200")
                sumRight += 200
        
        if count >= 15:
            if rover.laser_distances[count] != float('inf'):
                sumLeft += rover.laser_distances[count]
                #print("value:", rover.laser_distances[count])
            else:
                #print("Adding 200")
                sumLeft += 200

        count += 1
        #print(count)
    #print("sumLeft:", sumLeft)
    #print("sumRight:", sumRight)

    if sumLeft > sumRight:
        return "left"
            
    if sumRight > sumLeft:
        return "right"

    else:
        return "NOT WORKING"       

def main():  
    while not rospy.is_shutdown():
        
        if (objectivex - 0.8 <= rover.x <= objectivex + 0.8) and (objectivey - 0.8 <= rover.y <= objectivey + 0.8):
                print("Destination reached, terminating program...\n")
                left_side_speed = 0
                right_side_speed = 0
                rover.send_command(left_side_speed, right_side_speed)
                return 0
        
        #print("Moving forward...")
        #print("X: " + str(rover.x) + " Y: " + str(rover.y) + " Heading: " + str(rover.heading))
        #print (rover.laser_distances)

        for dist in rover.laser_distances:
            
            if dist < 2:
                whichWay = side_to_favour()
                #print(whichWay)

                if whichWay == "right":
                    print("Turning " + whichWay + "...\n")
                    turn_right(rover, left_side_speed, right_side_speed)
                    print("Finished turn!\n")
                    sleep(0.05)
                       
                if whichWay == "left":
                    print("Turning " + whichWay + "...\n")
                    turn_left(rover, left_side_speed, right_side_speed)
                    print("Finished turn!\n")
                    sleep(0.05)
                
            if ((rover.laser_distances[0] > 8) and
               (rover.laser_distances[3] > 8) and
               (rover.laser_distances[6] > 8) and
               (rover.laser_distances[9] > 8) and
               (rover.laser_distances[12] > 8) and
               (rover.laser_distances[15] > 8) and
               (rover.laser_distances[18] > 8) and
               (rover.laser_distances[21] > 8) and
               (rover.laser_distances[24] > 8) and
               (rover.laser_distances[27] > 8)):
                sleep(0.05)
                tempHeading = find_heading(rover, objectivex, objectivey)
                reset_heading(rover, left_side_speed, right_side_speed, tempHeading)
            
            else:
                left_side_speed = 3
                right_side_speed = 3
                rover.send_command(left_side_speed, right_side_speed)
                #print("Moving forward...")
                sleep(0.01)
            #print("Temp Heading: " + str(find_heading(rover, objectivex, objectivey)))
            #print("Actual Heading: " + str(rover.heading))

        sleep(0.05)

if __name__ == "__main__":
    main()
