#include "ros/ros.h"
#include "std_msgs/Int32.h"
#include <string>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <memory>
#include <unistd.h>
#include <sound_play/sound_play.h>



void back(){
  sound_play::SoundClient sc;
  sc.playWave("'/home/ubuntu/catkin_ws/src/mysound/soundfile/back.wav'");
  sleep(1);
}

void left(){
  sound_play::SoundClient sc;
  sc.playWave("'/home/ubuntu/catkin_ws/src/mysound/soundfile/left.wav'");
  sleep(1);
}

void leftback(){
  sound_play::SoundClient sc;
  sc.playWave("'/home/ubuntu/catkin_ws/src/mysound/soundfile/leftback.wav'");
  sleep(1);
}

void right(){
  sound_play::SoundClient sc;
  sc.playWave("'/home/ubuntu/catkin_ws/src/mysound/soundfile/right.wav'");
  sleep(1);
}

void rightback(){
  sound_play::SoundClient sc;
  sc.playWave("'/home/ubuntu/catkin_ws/src/mysound/soundfile/rightback.wav'");
  sleep(1);
}


/*//git자료
void playerCallback(const std_msgs::String::ConstPtr& msg) {
  FILE *gp;
  // const std::string filename = "warning1.mp3"; // filename of mp3 file
  std::string message;
  if (msg->data.find(".mp3") != std::string::npos) {
    message = "mpg123 -q " + msg->data;
  } else if (msg->data.find(".wav") != std::string::npos) {
    message = "aplay " + msg->data;
  }else{
    ROS_INFO("%s isn't a sound file.", msg->data.c_str());
  }

  if (!message.empty()) {
    char *cstr = new char[message.size() + 1]; // get memory
    std::strcpy(cstr, message.c_str());        // copy
    gp = popen(cstr, "w");
    pclose(gp); // パイプを閉じる

    ROS_INFO("playing %s", msg->data.c_str());
  }
}
*/



void playerCallback(const std_msgs::Int32::ConstPtr& msg){
  ROS_INFO("Recieved: [%d]", msg->data);
  int waydata = msg->data;
  if (waydata == 4){
    left();
  }
  else if (waydata ==1){
    leftback();
  }
  else if (waydata ==2){
    back();
  }
  else if (waydata ==6){
    right();
  }
  else if (waydata ==3){
    rightback();
  }
}



int main(int argc, char **argv) {

  // establish ros node
  ros::init(argc, argv, "mysound");//노드명 초기화
  ros::NodeHandle nh;//ros통신을 위한 node handle
  sound_play::SoundClient sc;

  ros::Subscriber sub = nh.subscribe("direction", 10, playerCallback);
  ROS_INFO("sound player is ready.");

  ros::spin();

}
