#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from playsound import playsound
from std_msgs.msg import Int32


def back():
        playsound("/home/ubuntu/catkin_ws/src/mysound/soundfile/sound_each/dir/back.wav")

def left():
        playsound("/home/ubuntu/catkin_ws/src/mysound/soundfile/sound_each/dir/backleft.wav")

def leftback():
        playsound("/home/ubuntu/catkin_ws/src/mysound/soundfile/leftback.wav")

def right():
        playsound("/home/ubuntu/catkin_ws/src/mysound/soundfile/right.wav")

def rightback():
        playsound("/home/ubuntu/catkin_ws/src/mysound/soundfile/rightback.wav")

def direction_callback(data):
                #keyboard ja apan cham go
                # (4:left), (1:leftback), (2:back), (6:right), (3:rightback)
                if(data.data == 4):
                        left()
                        rospy.loginfo("left sound is activated")
                elif(data.data == 1):
                        leftback()
                        rospy.loginfo("leftback sound is activated")
                elif(data.data == 2):
                        back()
                        rospy.loginfo("back sound is activated")
                elif(data.data == 6):
                        right()
                        rospy.loginfo("right sound is activated")
                elif(data.data == 3):
                        rightback()
                        rospy.loginfo("rightback sound is activated")


def main():
        rospy.init_node('mysound', anonymous=True)
        rospy.loginfo("sound module is actived")
        sub = rospy.Subscriber('direction', Int32, direction_callback)
        rospy.spin()


if __name__ == '__main__':
        try:
                main()
        except rospy.ROSInterruptException:
                pass
