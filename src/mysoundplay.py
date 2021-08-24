#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from playsound import playsound
from std_msgs.msg import Int32
import time


def back():
        playsound("/home/ubuntu/catkin_ws/src/mysound/soundfile/back.wav")

def left():
        playsound("/home/ubuntu/catkin_ws/src/mysound/soundfile/left.wav")

def leftback():
        playsound("/home/ubuntu/catkin_ws/src/mysound/soundfile/leftback.wav")

def right():
        playsound("/home/ubuntu/catkin_ws/src/mysound/soundfile/right.wav")

def rightback():
        playsound("/home/ubuntu/catkin_ws/src/mysound/soundfile/rightback.wav")

stackCreate = 0

def direction_callback(data):
        i=0
        global stackCreate
        while True:
                if stackCreate ==0:
                        stack = []
                        stackCreate = 1
                        break
        #rospy.loginfo("cho gi stack : %d", stack[0]) yo gi su error -> it means we ae seo reset
        set_time = time.time() + 5#5초 설정
        stack.append(data.data)
        #if time.time() > set_time:#설정한 시간지나면 스택 비움
        #        stack.clear()
        #        i = 0
                #if len(stack) > 20:#너무 많이 쌓이면 빠져나옴
                #        break

        rospy.loginfo("len stack : %d",len(stack))
        for i in range(len(stack)):
                rospy.loginfo("stack [%d] : %d",i,stack[i])
        #keyboard ja apan cham go
        # (4:left), (1:leftback), (2:back), (6:right), (3:rightback)

        if len(stack) >= 3:
                while True:
                        if(stack[i] == 4):
                                left()
                                rospy.loginfo("left sound is activated i : %d, stack[i] : %d",i, stack[i])
                        elif(stack[i] == 1):
                                leftback()
                                rospy.loginfo("leftback sound is activated i : %d, stack[i] : %d",i, stack[i])
                        elif(stack[i] == 2):
                                back()
                                rospy.loginfo("back sound is activated i : %d, stack[i] : %d",i, stack[i])
                        elif(stack[i] == 6):
                                right()
                                rospy.loginfo("right sound is activated i : %d, stack[i] : %d",i, stack[i])
                        elif(stack[i] == 3):
                                rightback()
                                rospy.loginfo("rightback sound is activated i : %d, stack[i] : %d",i, stack[i])

                        if(i >= len(stack)):
                                rospy.loginfo("stack will be clear")
                                stack.clear()
                                break
                        i=i+1
        rospy.loginfo("spin is jung sang")


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


