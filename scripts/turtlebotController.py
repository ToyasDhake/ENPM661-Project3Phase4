#!/usr/bin/env python

import rospy
from gazebo_msgs.msg import LinkState
from geometry_msgs.msg import Twist
from AStar import AStar
from time import sleep
import sys

def getRPM(action, stepSize):
    if action == "1":
        return 0, stepSize[1]
    if action == "2":
        return stepSize[0], stepSize[1]
    if action == "3":
        return stepSize[1], stepSize[1]
    if action == "4":
        return stepSize[1], stepSize[0]
    if action == "5":
        return stepSize[1], 0
    if action == "6":
        return 0, stepSize[0]
    if action == "7":
        return stepSize[0], stepSize[0]
    if action == "8":
        return  stepSize[0], 0

def main():
    rospy.init_node('location_monitor')
    cmd_publish = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1) # 10hz
    # to induce the wandering behaviour
    stepSize = [int(sys.argv[7]), int(sys.argv[8])]
    clearance = 5
    aStar = AStar([int((float(sys.argv[1])+5)*10), int((float(sys.argv[2])+5)*10), int(sys.argv[3])],
                  [int((float(sys.argv[4])+5)*10), int((float(sys.argv[5])+5)*10)], clearance+int(sys.argv[6]), stepSize)
    solution = aStar.solve()
    print(len(solution))
    temp = solution[0]
    for i in range(1, len(temp)):
        command = Twist()
        # to induce the linear motion
        #command.link_name = 'turtlebot3_burger::wheel_left_link'
        #command.angular.z = 0.6
        r = 0.0033
        l = 0.9

        action = temp[i].action
        rpm1, rpm2 = getRPM(action, stepSize)

        command.linear.x = r/2*(rpm1+rpm2)
        command.angular.z = r/l*(rpm1-rpm2)
        print(command.linear.x, command.angular.z)
        #command.twist = twist
        #command.reference_frame = "map"
        # to induce the angular motion
        cmd_publish.publish(command)
        sleep(10)
    command = Twist()
    command.linear.x = 0
    command.angular.z = 0
    cmd_publish.publish(command)
if __name__ == '__main__':
    main()
