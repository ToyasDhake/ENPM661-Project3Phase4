# ENPM661-ProjectThree
# A* algorithm for path planning of robot.

## Overview

Path planning is a problem that every mobile robot has to solve in order to
move around in its environment. There are multiple approaches to solve this
problem, one of which is A* algorithm. 
 
A* algorithm is a path searching algorithm which uses Heuristics to increase 
performance while maintaining optimality of the output. A* is very efficient
when compared to other primitive search algorithms such as brute force.  

## Dependencies

- Python 3.6.9
- ROS Melodic
- Turtlebot 3


## Demo Steps
```
paste project folder in src in catkin workspace
open terminal in catkin workspace
source devel/setup.bash
roslaunch ENPM661-Project3Phase4 demo.launch x_pos:=-4 y_pos:=-4 theta:=0 x_pos_f:=4 y_pos_f:=4 clearance:=0 rpm1:=60 rpm2:=30
```
Values of theta are in Radians.

## Results



## Contributors

- Toyas Dhake

- Loic Barret
