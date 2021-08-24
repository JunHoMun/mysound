#!/usr/bin/env python3

import rospy
from playsound import playsound
from std_msgs.msg import Int32MultiArray

SOUNDFILE = "/home/ubuntu/catkin_ws/src/mysound/soundfile/"
FILENAME = ("left.wav", "leftback.wav", "back.wav", "rightback.wav", "right.wav")

def direction_callback(data):
        for i in range(5):
                if data.data[i] > 0:
                        tmp = SOUNDFILE+FILENAME[i]
                        playsound(tmp)
                        tmp = FILENAME[i] + " sound is activated, dist :"
                        rospy.loginfo(tmp)
                        print(data.data[i])

def main():
        rospy.init_node('mysound', anonymous=True)
        sub = rospy.Subscriber('direction', Int32MultiArray, direction_callback)
        rospy.spin()

if __name__ == '__main__':
        try:
                main()
        except rospy.ROSInterruptException:
                pass
