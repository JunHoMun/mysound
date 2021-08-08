#!/usr/bin/env python

import rospy
from sound_play.libsoundplay import SoundClient
from std_msgs.msg import Int32


def back():
        sound_client = SoundClient()
        rospy.sleep(2)
        sound = sound_client.waveSound('/home/ubuntu/catkin_ws/src/mysound/soundfile/back.wav')
        sound.play()

def left():
        sound_client = SoundClient()
        rospy.sleep(2)
        sound = sound_client.waveSound('/home/ubuntu/catkin_ws/src/mysound/soundfile/left.wav')
        sound.play()

def leftback():
        sound_client = SoundClient()
        rospy.sleep(2)
        sound = sound_client.waveSound('/home/ubuntu/catkin_ws/src/mysound/soundfile/leftback.wav')
        sound.play()

def right():
        sound_client = SoundClient()
        rospy.sleep(2)
        sound = sound_client.waveSound('/home/ubuntu/catkin_ws/src/mysound/soundfile/right.wav')
        sound.play()

def rightback():
        sound_client = SoundClient()
        rospy.sleep(2)
        sound = sound_client.waveSound('/home/ubuntu/catkin_ws/src/mysound/soundfile/rightback.wav')
        sound.play()

def direction_callback(data):
                #keyboard ja apan cham go
                # (4:left), (1:leftback), (2:back), (6:right), (3:rightback)
                if(data.data == 4):
                        rospy.loginfo("left sound is activated")
                        left()
                elif(data.data == 1):
                        rospy.loginfo("leftback sound is activated")
                        leftback()
                elif(data.data == 2):
                        rospy.loginfo("back sound is activated")
                        back()
                elif(data.data == 6):
                        rospy.loginfo("right sound is activated")
                        right()
                elif(data.data == 3):
                        rospy.loginfo("rightback sound is activated")
                        rightback()

def main():
        rospy.init_node('mysound', anonymous=True)
        sub = rospy.Subscriber('direction', Int32, direction_callback)
        rospy.spin()


if __name__ == '__main__':
        try:
                main()
        except rospy.ROSInterruptException:
                pass
