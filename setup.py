# this set of lines is to make sure that the python scripts can find the ROS libraries
import sys
sys.path.append('/opt/ros/noetic/lib/python3/dist-packages')
sys.path.append('/usr/lib/python3/dist-packages')

import os

# change the ROS environment variable to th.lan.robolabe robot's IP address
ROBOT_HOSTNAME = 'robotics10' # for example, this could be an IP or a hostname depending on what is reachable on the network
CONSOLE_HOSTNAME = 'group10' # for example, notice that this is the IP of the computer running this script not the robot

# another example using hostnames is as follows
# ROBOT_HOSTNAME = 'robotics1' # for example, this could be an IP or a hostname depending on what is reachable on the network
# CONSOLE_HOSTNAME = 'group1' # for example, notice that this is the hostname of the computer running this script not the robot

# the following lines set up the networking variables for the scripts to run properly
os.environ['ROS_MASTER_URI'] = 'http://{}:11311'.format(ROBOT_HOSTNAME)
os.environ['ROS_HOSTNAME'] = CONSOLE_HOSTNAME
print('connected')