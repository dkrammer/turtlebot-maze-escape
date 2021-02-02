#! /usr/bin/env python

import rospkg
import rospy
import sys
# Import the service message used
from std_srvs.srv import Trigger, TriggerRequest

# Initialise node
rospy.init_node('crash_service_client')

# Wait for the service to be running
rospy.wait_for_service('/crash_service')

# Create the connection to the service
crash_service_connection = rospy.ServiceProxy('/crash_service', Trigger)

# Create an object of type TriggerRequest()
crash_object = TriggerRequest()

# Send through the connection the name of the trajectory to be executed by the robot
result = crash_service_connection(crash_object)

# Print the result given by the service called
print(result)