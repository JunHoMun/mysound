#include "ros/ros.h"
#include "std_msgs/Int32.h"
#include <string>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <memory>
#include <unistd.h>
#include <sound_play/sound_play.h>

int main(int argc, char **argv){
  ros::init(argc, argv, "testpub");
  ros::NodeHandle n;
  ros::Publisher pub = n.advertise<std_msgs::Int32>("/direction", 10);
  ros::Rate loop_rate(10);

  int waydata;
  ROS_INFO("input data :");
  scanf("%d", &waydata);

  while(ros::ok()){
    std_msgs::Int32 msg;
    ROS_INFO("%d is input", msg.data);
    pub.publish(msg);
    ros::spin();
    loop_rate.sleep();
  }
  return 0;
}
