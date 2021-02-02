#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

class OdometryClass():
    
    def __init__(self):
        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.callback)
        self.odom = Odometry()
        self.exit_topic = False
        self.rate = rospy.Rate(1) # 10hz

    def callback(self, msg):
        print("\nx: ", msg.pose.pose.position.x)
        print("y: ", msg.pose.pose.position.y)
        print("z: ", msg.pose.pose.position.z)
        self.rate.sleep()


        
if __name__ == '__main__':
    rospy.init_node('odom_turtlebot_test')
    odom_turtle_object = OdometryClass()
    try:
        #blah blah blah
        '''
        blah
        blah
        blah
        '''
    except rospy.ROSInterruptException:
        pass