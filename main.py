# import python libraries
import rospy # ros library for python
from sensor_msgs.msg import Illuminance
from geometry_msgs.msg import Twist

# create a class to subscribe to sensor messages and show the data
class RoverIlluminanceController:
    spin_threshold = 300  # threshold to trigger spinning
    spin_speed = 1.0  # spin speed
    stop_speed = 0.0  # stop speed
    
    def __init__(self):
        rospy.init_node('rover_illuminance_controller', anonymous=True)
        
        self.illuminance = 0.0
        self.twist = Twist()
        
        self.illuminance_sub = rospy.Subscriber('/rvr_driver/ambient_light', Illuminance, self.callback)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        
        print('controller node started')       

    # callback function to receive the data
    def callback(self, msg):
        # print the data received
        self.illuminance = msg.illuminance
        print(f'illumincance: {self.illuminance}')
        
        #check if rover should be spinning
        self.update_rover_motion()
            
    def update_rover_motion(self):
        #updates motion based on the illuminance
        if self.illuminance >= self.spin_threshold:
            self.set_rover_spin(self.spin_speed)
        else:
            self.set_rover_spin(self.stop_speed)
            
            
    def set_rover_spin(self, speed):
        #control rover spin
        self.twist.angular.z = speed
        self.cmd_vel_pub.publish(self.twist)
        print('rover spinning' if speed else 'rover stopped spinning')

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    try:
        controller = RoverIlluminanceController()
        controller.run()
    except rospy.ROSInterruptException:
        ("Rover Illuminance Controller Node Interrupted")
    finally:
        rospy.loginfo("Node Shutdown")
