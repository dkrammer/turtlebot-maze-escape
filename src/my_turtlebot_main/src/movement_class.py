#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class MovementClass():
    
    def __init__(self):
        self.movement_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.move = Twist()
        self.exit_topic = False
        self.freq = 10
        self.rate = rospy.Rate(self.freq) # 10hz
        rospy.on_shutdown(self.shutdown)
        
    def publish_info(self):
        # Method taken from "Using Python Classes in ROS" segment
        while not self.exit_topic:
            connections = self.movement_publisher.get_num_connections()
            if connections > 0:
                self.movement_publisher.publish(self.move)
                #rospy.loginfo("Cmd Published")
                break
            else:
                self.rate.sleep()
        
    def shutdown(self):
        self.stop_moving() # Make turtle stop on shutdown
        self.exit_topic = True
        

    def move_forward(self, linear_speed=0.5, angular_speed=0.0):
        rospy.loginfo("Moving forward")

        self.move.linear.x = linear_speed
        self.move.angular.z = angular_speed
        self.publish_info()


    def turn(self, linear_velocity=0.5, angular_velocity=0.5):
        # At a rate of 10 Hz, it takes
        # pi s to turn pi/2 rad when 
        # |angular velocity| = 0.5 rad/s
        
        # This achieves a turning radius
        # of 0.5m

        hz = 30
        self.move.linear.x = linear_velocity
        self.move.angular.z = angular_velocity
        self.publish_info()

        while (hz != 0):
            hz -= 1
            self.rate.sleep()

        self.move.angular.z = 0.0
        self.publish_info()

    def turn_right(self, linear_velocity=0.2618):
        rospy.loginfo("Turning right")
        angular_velocity = 0.475

        self.turn(linear_velocity, angular_velocity)
        rospy.loginfo("Turned right")
       

    def turn_left(self, linear_velocity=0.2618):
        rospy.loginfo("Turning left")
        angular_velocity = -0.53
        
        self.turn(linear_velocity, angular_velocity)
        rospy.loginfo("Turned left")

    def stop_moving(self):
        self.move.linear.x = 0
        self.move.angular.x = 0
        self.publish_info()
        rospy.loginfo("Stopped")


if __name__ == '__main__':
    rospy.init_node('move_turtlebot_test')
    move_turtle_object = MovementClass()
    try:

        move_turtle_object.move_forward(seconds=7, linear_speed=0.5)
        move_turtle_object.turn_right()
        move_turtle_object.move_forward(seconds=5, linear_speed=0.5)

        
        move_turtle_object.stop_moving()
    except rospy.ROSInterruptException:
        pass