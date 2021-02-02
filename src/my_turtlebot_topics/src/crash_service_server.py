#! /usr/bin/env python

import rospy
from std_srvs.srv import Trigger, TriggerResponse
from laser_scan_class import LaserScanClass


def crash_callback(request):
    rospy.loginfo("The service /crash_service has been called")
    response = TriggerResponse()

    # get data from laser scan class
    # LaserScanClass attributes available:
    # turn_direction: String
    # crashing: Bool
    # exited_maze: Bool

    # Check if robot has exited maze
    if crash_object.exited_maze:
        response.success = True
    else:
        response.success = False

    # Check if robot is about to crash
    if crash_object.crashing:
        # crash threshold is ~1m
        # about to crash, send turn request
        #response.success = True
        response.message = crash_object.turn_direction
    else:
        #keep going straight
        response.message = "straight"
        #response.success = False

    #print(response.success)
    #print(response.message)

    # if about to crash,
    # response.success = True -> about to crash, make robot turn
    # else,
    # response.success = False
    # response.message = "straight" -> not about to crash, robot continues straight


    # if wall in front and on left, turn right
    # response.message = "right"

    # elif wall in front and on right, turn left
    # response.message = "left"

    



    # if no wall in front,          OR          if escaped maze,
    # response.success = True                   response.success = True
    # if about to crash,                        if not escaped maze,
    # response.success = False                  response.success = False
    
    print("crash_callback has been called")
    return response
    #return MyServiceResponse(len(request.words.split())) 

rospy.init_node('service_crash_server') 
crash_service = rospy.Service('/crash_service', Trigger , crash_callback)

rospy.loginfo("Crash Service Ready")
crash_object = LaserScanClass()

rospy.spin()