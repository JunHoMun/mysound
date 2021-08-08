#!/usr/bin/env python
# -*- coding: utf-8 -*-


import rospy
from std_msgs.msg import Int32

def talker():
    pub = rospy.Publisher('direction', Int32, queue_size=10)
    rospy.init_node('testpub', anonymous=True)
    rate = rospy.Rate(1) # 초당 n번 발행
    while not rospy.is_shutdown():
        inputdat = input('input any direction: ')
        inputdata = int(inputdat)
        rospy.loginfo("input data : %d" %(inputdata))
        pub.publish(inputdata)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
