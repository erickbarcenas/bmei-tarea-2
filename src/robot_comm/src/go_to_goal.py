#!/usr/bin/python3

from math import atan2
from numpy.lib.function_base import angle
import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2
from std_msgs.msg import String


class GoToGoal():
    def __init__(self):
        self.goal = Point()
        self.goal.x = 2.0
        self.goal.y = 2.0
        self.mov_msg = Twist()

        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

    
        self.mov_dic_fast = {
                'avanza':   [0.5 , 0.0],
                'gira':     [0.0 , 0.5],
                'detente':  [0.0, 0.0]
            }
        
        self.mov_dic_slow = {
                'avanza':   [0.05 , 0.0],
                'gira':     [0.0 , 0.05],
                'detente':  [0.0, 0.0]
            }

        # Creating the publisher with data type Twist (instead String)
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1) # cmd_vel is the topic
        
        # Creating the subscriber
        # rospy.Subscriber('/recognizer/output', String, callback=self.get_mov) # Subscribes to the /recognizer/output topic
        self.sub = rospy.Subscriber("/odom", Odometry, callback=self.callback_odom)

        

        rate = rospy.Rate(1) # 1 Hz

        # Below you write what you want to be published
        while not rospy.is_shutdown(): # While not pressing ctrl + c
            
            inc_x = self.goal.x - self.x
            inc_y = self.goal.y - self.y

            print(f"goal x: {self.goal.x}  ---- x:{self.x}")
            print(f"goal y: {self.goal.y}  ---- y:{self.y}")

            if inc_x == 0.0 and inc_y == 0.0:
                    get_key = self.mov_dic_slow['avanza']
                    self.mov_msg.linear.x = get_key[0] # X
                    self.mov_msg.angular.z = get_key[1] # Z
                    print('Meta alcanzada')
            else:
                angle_to_goal = atan2(inc_y, inc_x)

                if abs(angle_to_goal - self.theta) > 0.1:
                    # gira
                    if inc_x < 1.0 and inc_y < 1.0:
                        print('---- gira slow ----')
                        get_key = self.mov_dic_slow['gira']
                    else:
                        print('---- gira fast ----')
                        get_key = self.mov_dic_fast['gira']
                    
                    self.mov_msg.linear.x = get_key[0] # X
                    self.mov_msg.angular.z = get_key[1] # Z
                else:
                    # avanza
                    if inc_x < 1.0 and inc_y < 1.0:
                        print('---- avanza slow ----')
                        get_key = self.mov_dic_slow['avanza']
                    else:
                        print('---- avanza fast ----')
                        get_key = self.mov_dic_fast['avanza']
                    
                    self.mov_msg.linear.x = get_key[0] # X
                    self.mov_msg.angular.z = get_key[1] # Z
                self.pub.publish(self.mov_msg)
                #print(self.mov_msg) # Shown on the console
                rate.sleep() 



    def callback_odom(self, msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        rot_q = msg.pose.pose.orientation

        (roll, pitch, self.theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
    

    def get_mov(self, mov): # The topic passes the value 'mov'
        key_txt = mov.data
        if key_txt in self.mov_dic:
            get_key = self.mov_dic[key_txt]
            self.mov_msg.linear.x = get_key[0]
            self.mov_msg.angular.z = get_key[1]

            print('Command executed successfully')
        else:
            self.stop()
            print('Command not recognized.')
            print('The recognized commands are the following three: avanza, gira y detente')




# Function that initializes the node
def init_node():
    rospy.init_node('action_pub', anonymous=True)
    print('Node created successfully!')

if __name__ == '__main__':
    init_node()
    try:
        GoToGoal() 
    except rospy.ROSInterruptException:
        pass