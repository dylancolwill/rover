"""receiving message data"""


# import python libraries
import rospy # ros library for python
from sensor_msgs.msg import Illuminance # import the Imu message type definition

illuminance =0

# create a class to subscribe to sensor messages and show the data
class SubscribeAndShowNode(object):
    def __init__(self):
        global illuminance
        # subscribe to the topic ~imu from the rvr namespace
        
        self.imu_sub = rospy.Subscriber('/rvr_driver/ambient_light', Illuminance, self.callback)
        
        print(illuminance)
        

    # callback function to receive the data
    def callback(self, msg):
        
        # print the data received
        illuminance =msg.illuminance
        print(f'illuminance: {illuminance}')
        
        if illuminance >= 300:
            self.rover_spin()
        else:
            self.rover_stop_spin()
            
    def rover_spin(self):
        self.twist.angular.z = 1.0  #spin speed
        self.cmd_vel_pub.publish(self.twist)

    def rover_stop_spin(self):        
        self.twist.angular.z = 0.0
        self.cmd_vel_pub.publish(self.twist)

            
# main function
def main():
    try:
        # initialize the node with rospy
        rospy.init_node('subscribe_and_show_node', anonymous=True)

        # create an instance of the SubscribeAndShowNode class
        # this will subscribe to the topic and show the data
        sub_show_node = SubscribeAndShowNode()

        # spin() simply keeps python from exiting until this node is stopped
        print(illuminance)
        rospy.spin()

    except rospy.ROSInterruptException as e:
        print(e)
    finally:
        print('Node has shutdown')

main()
print('the SubscribeAndShowNode class has been declared')
