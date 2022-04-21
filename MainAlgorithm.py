# Importing libraries, objects and defining the destination in x and y.
from qset_lib import Rover
from time import sleep
import rospy
import math
rover = Rover()
rover.laser_distances = [0] * 30
sum1 = 0
sum2 = 0
objectivex = 15 # Destination of the x-coordinate, which is the red axis in gazebo
objectivey = 1 # Destination of the y-coordinate, which is the green axis in gazebo

# Function to turn the rover left.
def turn_left(rover, left_speed, right_speed):
    while(1):
        # Set the left speed to 0 and the right speed to 3 to turn the rover left.
        left_side_speed = 0
        right_side_speed = 3
        rover.send_command(left_side_speed, right_side_speed)
        sleep(0.4)
        break

# Function to turn the rover right.        
def turn_right(rover, left_speed, right_speed):
    while(1):
        # Set the right speed to 0 and the left speed to 3 to turn the rover right.
        left_side_speed = 3
        right_side_speed = 0
        rover.send_command(left_side_speed, right_side_speed)
        sleep(0.4)
        break

# Function to find the new heading angle after the rover turns (returns heading angle).
def find_heading(rover, objectivex, objectivey):
    #Finds the slope between the two points relative to the x-axis (0 degrees).
    m = (objectivey-rover.y)/(objectivex-rover.x) 
    
    # Series of if-statements determining and returning the heading angle to the destination depending on the quadrant the rover is in
    # and the direction to the destination (upper-left, upper-right, bottom-left, bottom-right).
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

# Function to turn the rover towards the destination.
def reset_heading(rover, left_side_speed, right_side_speed, tempHeading):
    # If the rover is pointed towards the destination, go straight.
    if (tempHeading+1>rover.heading>tempHeading-1):
        left_side_speed = 4
        right_side_speed = 4
        rover.send_command(left_side_speed, right_side_speed)
        print("Destination is straight ahead...\n")
        sleep(0.1)
        return
    # If the rover needs to adjust left, turn left.
    if (tempHeading>rover.heading>-179.99):
        left_side_speed = 0
        right_side_speed = 3
        rover.send_command(left_side_speed, right_side_speed)
        print("Turning left towards destination...\n")
        sleep(0.1)
    
    # If the rover needs to adjust right, turn right.
    if (tempHeading<rover.heading<179.99):
        left_side_speed = 3
        right_side_speed = 0
        rover.send_command(left_side_speed, right_side_speed)
        print("Turning right towards destination...\n")
        sleep(0.1)
            
# Function to determine the favorable side to turn (Left or Right).
def side_to_favour():
    sumRight = 0
    sumLeft = 0
    count = 0
#sum both the left (0-15) and right (15-29) laser distances, set any values of 'infinity' to 200 so that they can be properly added.
    while(count <= 29):
        if count <= 15:
            if rover.laser_distances[count] != float('inf'):
                sumRight += rover.laser_distances[count]
            else:
                sumRight += 200
        if count >= 15:
            if rover.laser_distances[count] != float('inf'):
                sumLeft += rover.laser_distances[count]
            else:
                sumLeft += 200
        count += 1
#return the side that has the least obstacles (higher sum (further distances))
    if sumLeft > sumRight:
        return "left"
    if sumRight > sumLeft:
        return "right"
    else:
        return "NOT WORKING"       

# The main function.
def main():  
    # Print the final destination.
    print("Destination in x: " + str(objectivex))
    print("Destination in y: " + str(objectivey) + "\n")
    # Keep the going until the rover is shut down or the rover reaches its destination.
    while not rospy.is_shutdown():
        # If the rover is right on or super close to its destination, stop the rover and terminate the program.
        if (objectivex - 0.8 <= rover.x <= objectivex + 0.8) and (objectivey - 0.8 <= rover.y <= objectivey + 0.8):
                print("Destination reached, terminating program...\n")
                left_side_speed = 0
                right_side_speed = 0
                rover.send_command(left_side_speed, right_side_speed)
                return 0

        for dist in rover.laser_distances:
            # If the rover is within 4 m of an obstacle in front (or 1.2 m on the sides), decide which way to turn and turn that way until the obstacle is no longer in the way.
            if (rover.laser_distances[13] < 4 or rover.laser_distances[14] < 4 or rover.laser_distances[15] < 4 or rover.laser_distances[16] < 4
               or rover.laser_distances[0] < 1.2 or rover.laser_distances[2] < 1.2 or rover.laser_distances[4] < 1.2 or rover.laser_distances[6] < 1.2
               or rover.laser_distances[8] < 1.2 or rover.laser_distances[10] < 1.2 or rover.laser_distances[12] < 1.2 or rover.laser_distances[18] < 1.2
               or rover.laser_distances[20] < 1.2 or rover.laser_distances[22] < 1.2 or rover.laser_distances[24] < 1.2 or rover.laser_distances[26] < 1.2
               or rover.laser_distances[28] < 1.2):
                whichWay = side_to_favour()
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
            # Pick some LiDAR values and check if they all indicate the rover is at least 6 m from an obstacle. 
            # If the rover is, reset the heading to reach the destination.
            if ((rover.laser_distances[3] > 6) and (rover.laser_distances[6] > 6) and (rover.laser_distances[9] > 6) and
               (rover.laser_distances[12] > 6) and (rover.laser_distances[15] > 6) and (rover.laser_distances[18] > 6) and
               (rover.laser_distances[21] > 6) and (rover.laser_distances[24] > 6) and (rover.laser_distances[27] > 6)):
                
                sleep(0.05)
                tempHeading = find_heading(rover, objectivex, objectivey)
                reset_heading(rover, left_side_speed, right_side_speed, tempHeading)
            # Otherwise, go straight.
            else:
                left_side_speed = 3
                right_side_speed = 3
                rover.send_command(left_side_speed, right_side_speed)
                sleep(0.01)

        sleep(0.05)

if __name__ == "__main__":
    main()
