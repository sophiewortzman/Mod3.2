#Pseudocode from the Word doccument

Functions?
Set up lidar sensor to be read
Integrate steering libraries to control rover,
Integrate headings and location data

While (endpoint does not equal current point) {
  Move towards object
  if (LiDAR detects obstacle) {
    Run Dijkstra’s algorithm {
    }
    Follow path towards end. 
  } else stop moving 


Code snippets: https://gitlab.com/qset-mod-3/unified-launch/

Tasks: 
Integrate steering libraries to control rover
Integrate headings and location data
Retrieve LiDAR data using Python libraries
Create loop continuing until the target is reached
Create the irregular obstacle avoidance algorithm
Implement Dijkstra’s Algorithm
