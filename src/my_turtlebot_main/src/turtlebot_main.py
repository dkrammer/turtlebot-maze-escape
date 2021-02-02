#! /usr/bin/env python

import rospkg
import rospy
import sys
from std_srvs.srv import Trigger, TriggerRequest
from movement_class import MovementClass

def main():

    rospy.init_node('crash_service_client')
    rospy.wait_for_service('/crash_service')
    crash_service_connection = rospy.ServiceProxy('/crash_service', Trigger)

    move_turtle_object = MovementClass()
    crash_object = TriggerRequest()

    start_time = rospy.get_time()
    print("Start time:", start_time)


    while 1:
        result = crash_service_connection(crash_object)
        
        # Update start time as it begins at 0
        # and then jumps to somewhere in the thousands
        # once robot starts moving
        if (start_time == 0):
            start_time = rospy.get_time()
            print(start_time)

        if result.success: # exited the maze, stop robot
            move_turtle_object.stop_moving()
            rospy.loginfo("Exited the maze")
            break

        if result.message == "left": # turn left
            move_turtle_object.turn_left()

        elif result.message == "right": # turn right
            move_turtle_object.turn_right()
        else: # go straight
            move_turtle_object.move_forward()

    end_time = rospy.get_time()
    total_time = end_time - start_time
    print("Time taken:", total_time)

main()

