#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

class LaserScanClass():
    
    def __init__(self):
        self.laser_sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, self.callback)
        self.scan = LaserScan()
        self.crash_threshold = 2
        self.crashing = False
        self.turn_direction = "straight"
        self.exited_maze = False
        self.rate = rospy.Rate(10) # 10hz
    
    def callback(self, msg):
        #print("\nrunning")

        self.exited_maze = self.turtle_exited_maze(msg)
        self.crashing = self.about_to_crash(msg)
        if self.crashing:
            self.turn_direction = self.get_turn_direction(msg)
        else:
            self.turn_direction = "straight"

        #self.rate.sleep()
    
    def scan_front(self, msg):
        return msg.ranges[360]

    def scan_right(self, msg):
        return msg.ranges[0]

    def scan_left(self, msg):
        return msg.ranges[719]

    def get_turn_direction(self, msg):
        front_wall_distance = self.scan_front(msg)
        right_wall_distance = self.scan_right(msg)
        left_wall_distance = self.scan_left(msg)

        if (front_wall_distance > right_wall_distance) and (front_wall_distance > left_wall_distance):
            return "stright"
        elif right_wall_distance > left_wall_distance:
            return "right"
        else:
            return "left"

    def about_to_crash(self, msg):
        # crash threshold is ~1.5m (tweak)
        if self.scan_front(msg) < self.crash_threshold:
            return True
        else:
            return False
    
    def turtle_exited_maze(self, msg):
        front_dist = self.scan_front(msg)
        right_dist = self.scan_right(msg)
        left_dist = self.scan_left(msg)
        if (front_dist == right_dist) and (front_dist == left_dist):
            return True
        else:
            return False


if __name__ == '__main__':
    rospy.init_node('scan_turtlebot_test')
    scan_turtle_object = LaserScanClass()
    try:
        print("test")

    except rospy.ROSInterruptException:
        pass