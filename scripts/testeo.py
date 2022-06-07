#!/usr/bin/env python3

import sys

import roslib
import rospy

from fiducial_msgs.msg import FiducialArray

class ControlLoop:

    def __init__(self):
        self.subscriber = rospy.Subscriber("fiducial_vertices",
            FiducialArray, self.callback,  queue_size = 1)

    def callback(self, msg):
        print("Callback")


def main(args):
    c = ControlLoop()
    rospy.init_node('control', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down ROS controller")


if __name__ == '__main__':
    main(sys.argv)
