#Dermot's code for mars rover steering

# Useful files: 

# control.py -> converts quaternion data into roll, pitch and yaw data, stabilizes it by sending through PID. Publishes 64 multi-array and errors in r,p,y. 
# Initiates "control" node to control the rover. Publishes velocities of individual motors, recieves pose and sends msg, velPub, err_rollPub ... to 
# control_kwad


# PID -> outputs roll, pitch and yaw. Publishes motor velocities to 'f'. View convention: green goes left, red forward, blue up. Returns f, and the error
# in the roll, pitch and yaw to the control file. 


# gazebo_wheels_sabertooth -> publishes wheel commands, returns speed. 


# gazebo_wheels -> publishes wheel commands, temporary wheel data (fr, fl, ...). Publishes headings.  
