#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class MoveRobot():
    def __init__(self):

        # Creating the publisher with data type Twist (instead String)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) # cmd_vel is the topic
        
        # Creating the subscriber
        self.sub = rospy.Subscriber("/scan", LaserScan, self.scan_callback) # scan is the topic
        
        self.left = 0.0
        self.back = 0.0
        self.right = 0.0
        self.front = 0.0
        self.ctrl_c = False

        self.mov_dic = {
            'avanza':   [0.15 , 0.0],
            'gira':     [0.0 , 0.5],
            'detente':  [0.0, 0.0]
        }

        self.rate = rospy.Rate(1) # 1 Hz
        rospy.on_shutdown(self.shutdown)

    def scan_callback(self, msg):
        self.left = msg.ranges[90]
        self.back = msg.ranges[int(len(msg.ranges)/2)]
        self.right = msg.ranges[270]
        self.front = msg.ranges[1]

    def read_laser(self):
        while not self.ctrl_c:
            if self.back > 5:
                self.back = 5
            if self.left > 5:
                self.left = 5
            if self.right > 5:
                self.right = 5
            
            str_front = str(self.front)
            str_back = str(self.back)
            str_right = str(self.right)
            str_left = str(self.left)

            print(f"front = {str_front},  back = {str_back},  right = {str_right},  left = {str_left}")

    def shutdown(self):
        self.ctrl_c = True

    def main(self):
        self.out_of_maze = False
        self.mov_msg = Twist()

        while not self.out_of_maze:
            print(self.front) # Shown on the console
            if self.front > 1.0:
                key_txt = 'avanza'
                get_key = self.mov_dic[key_txt]
                self.mov_msg.linear.x = 0.25 # get_key[0] # linear speed
                self.mov_msg.angular.z = 0.0 # get_key[1] # angular speed
            else:
                key_txt = 'detente'
                get_key = self.mov_dic[key_txt]
                self.mov_msg.linear.x = 0.0 # get_key[0] # linear speed
                self.mov_msg.angular.z = 0.0 # get_key[1] # angular speed
            
            self.pub.publish(self.mov_msg)
            self.rate.sleep()

# Function that initializes the node
def init_node():
    rospy.init_node('action_pub', anonymous=True)
    print('Node created successfully!')

if __name__ == '__main__':
    rospy.init_node('action_pub', anonymous=True)
    move_robot = MoveRobot()
    try:
        move_robot.main() 
    except rospy.ROSInterruptException:
        pass