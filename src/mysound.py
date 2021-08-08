#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from sound_play.libsoundplay import SoundClient
from std_msgs.msg import Int32
from collections import deque#to make FIFO, i need this
import time


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
        queue = deque()
        t=time.time()+3#3초 설정
        #while len(queue) < 15:
        while time.time() < 5:#5초동안 반복
                queue.append(data.data)
                if len(queue) > 20:#queue 너무 많으면 빠져나옴
                        break
        count_left =0
        count_leftback =0
        count_back =0
        count_right =0
        count_rightback =0

        #각 숫자(방향)별로 카운트(많이 뜨는 방향 판단)
        for i in range(len(queue)):
                if queue[i] == 4:
                        count_left += 1
                elif queue[i] == 1:
                        count_leftback += 1
                elif queue[i] == 2:
                        count_back += 1
                elif queue[i] == 6:
                        count_right += 1
                elif queue[i] == 3:
                        count_rightback += 1



        #방향 판단
        temp = max(count_left, count_leftback, count_back, count_right, count_rightback)
        counttemp = 0
        real_direction = 0
        two_direction = 0
        while counttemp == 1:
                if counttemp > 1:#이건 2개 이상의 방향의 빈도가 같을경우
                        break#일단 반복문에서 나가서 해결한다.
                elif count_left == temp:
                        real_direction = count_left
                        counttemp +=1
                elif count_leftback == temp:
                        real_direction = count_leftback
                        counttemp +=1
                elif count_back == temp:
                        real_direction = count_back
                        counttemp +=1
                elif count_right== temp:
                        real_direction = count_right
                        counttemp +=1
                elif count_rightback== temp:
                        real_direction = count_rightback
                        counttemp +=1

        #양방향 판단
        if real_direction == 0:#counttemp>1
                if count_left == temp and count_leftback == temp:#좌&좌후
                        two_direction = 41
                elif count_left == temp and count_back == temp:#좌&후
                        two_direction = 42
                elif count_left == temp and count_right == temp:#좌&우
                        two_direction = 46
                elif count_left == temp and count_rightback == temp:#좌&우후
                        two_direction = 43
                elif count_leftback == temp and count_back == temp:#좌후&후
                        two_direction = 12
                elif count_leftback == temp and count_right == temp:#좌후&우
                        two_direction = 16
                elif count_leftback == temp and count_rightback == temp:#좌후&우후
                        two_direction = 13
                elif count_back == temp and count_right == temp:#후&우
                        two_direction = 26
                elif count_back == temp and count_rightback == temp:#후&우후
                        two_direction = 23
                elif count_right == temp and count_rightback==temp:#우&우후
                        two_direction = 63
                else:
                        pass

        # 앞으로 코딩방향 : stack에서 제일 많이 저장된 방향을 소리출력
        # 그리고 2개 이상의 방향을 소리출력하는 방안도 마련

        # 목 : 시간측정하는 방법 구하고, 3초 지나면 while문 빠져나오도록 설계한다.
        # 그리고 stack에서 각 숫자(방향)별로 카운트한다.



        #queue[:] = [] this make list empty
        #append, appendleft, pop, popleft





	#keyboard ja pan cham go
	# (4:left), (1:leftback), (2:back), (6:right), (3:rightback)
        if real_direction == 4:
                left()
        elif real_direction == 1:
                leftback()
        elif real_direction == 2:
                back()
        elif real_direction == 6:
                right()
        elif real_direction == 3:
                rightback()
        elif two_direction == 0:
                pass







def main():
        rospy.init_node('mysound', anonymous=True)
        sub = rospy.Subscriber('direction', Int32, direction_callback)
        rospy.spin()


if __name__ == '__main__':
        try:
                main()
        except rospy.ROSInterruptException:
                pass
