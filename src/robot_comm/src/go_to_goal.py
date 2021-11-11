#!/usr/bin/python3

from math import atan2
from numpy.lib.function_base import angle
import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from sensor_msgs.msg import LaserScan
from math import atan2
from std_msgs.msg import String


class MoveRobot(object):
    def __init__(self, x=2.0,y=2.0, vel_fast=0.5):
        self.goal = Point()
        self.goal.x = x
        self.goal.y = y
        self.mov_msg = Twist()

        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        self.vel_fast = vel_fast

    
        self.mov_dic_fast = {
                'avanza':   [self.vel_fast , 0.0],
                'gira':     [0.0 , self.vel_fast/3]
            }
        
        self.mov_dic_slow = {
                'avanza':   [0.1 , 0.0],
                'gira':     [0.0 , 0.1],
                'detente':  [0.0, 0.0]
            }

        # Scanner
        self.left = 0.0
        self.back = 0.0
        self.right = 0.0
        self.front = 0.0
        self.ctrl_c = False

        # Creating the subscriber
        # rospy.Subscriber('/recognizer/output', String, callback=self.get_mov) # Subscribes to the /recognizer/output topic
        self.sub = rospy.Subscriber("/odom", Odometry, callback=self.callback_odom)

        self.sub = rospy.Subscriber("/scan", LaserScan, self.scan_callback) # scan is the topic

        # Creating the publisher with data type Twist (instead String)
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1) # cmd_vel is the topic
        

        self.rate = rospy.Rate(5) # 5 Hz
        rospy.on_shutdown(self.shutdown)


    def scan_callback(self, msg):
        self.left = msg.ranges[90]
        self.back = msg.ranges[int(len(msg.ranges)/2)]
        self.right = msg.ranges[270]
        self.front = msg.ranges[1]

    def read_laser(self):
        if self.front <= 2.5:
            # gira a la derecha 90°
            self.mov_msg.linear.x = 0.0 # X
            self.mov_msg.angular.z = 1.5708 # Z   # giro 90°
            self.pub.publish(self.mov_msg)
            self.rate.sleep()

            # avanzo
            self.mov_msg.linear.x = 4.0 # X
            self.mov_msg.angular.z = 0.0 # Z   # giro 0°
            self.pub.publish(self.mov_msg)
            self.rate.sleep()

            # detente
            self.mov_msg.linear.x = 0.0 # X
            self.mov_msg.angular.z = 0.0 # Z   # giro 90°


        if self.back > 5:
            self.back = 5
        if self.left > 5:
            self.left = 5
            # avanzo
            self.mov_msg.linear.x = 4.0 # X
            self.mov_msg.angular.z = 0.0 # Z   # giro 0°
        if self.right > 5:
            self.right = 5
            # avanzo
            self.mov_msg.linear.x = 4.0 # X
            self.mov_msg.angular.z = 0.0 # Z   # giro 0°


            
            str_front = str(self.front)
            str_back = str(self.back)
            str_right = str(self.right)
            str_left = str(self.left)
            print(f"front = {str_front},  back = {str_back},  right = {str_right},  left = {str_left}")

    def shutdown(self):
            self.ctrl_c = True
            self.out_of_maze = True

         
    def callback_odom(self, msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        rot_q = msg.pose.pose.orientation

        (roll, pitch, self.theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
    

    def main(self):
        self.out_of_maze = False
        self.mov_msg = Twist()

        while not self.out_of_maze:

            diff_x = round(self.goal.x - self.x, 1)
            diff_y = round(self.goal.y - self.y, 1) # rounding to two decimal places

            print(f"diff_x: {diff_x}")
            print(f"diff_y: {diff_y}")

            if diff_x == 0.0 and diff_y == 0.0:
                    get_key = self.mov_dic_slow['detente']
                    self.mov_msg.linear.x = get_key[0] # X
                    self.mov_msg.angular.z = get_key[1] # Z
                    self.pub.publish(self.mov_msg)
                    self.rate.sleep()
                    
                    print('Meta alcanzada')
                    self.shutdown()
            else:
                angle_to_goal = atan2(diff_y, diff_x)

                if abs(angle_to_goal - self.theta) > 0.1:
                    # gira
                    if diff_x < 1.0 and diff_y < 1.0:
                        print('---- gira slow ----')
                        get_key = self.mov_dic_slow['gira']
                    else:
                        print('---- gira fast ----')
                        get_key = self.mov_dic_fast['gira']
                    
                    self.mov_msg.linear.x = get_key[0] # X
                    self.mov_msg.angular.z = get_key[1] # Z
                else:
                    # avanza mientras no haya objeto enfrente
                    if self.front > 2.5:
                        key_txt = 'avanza'
                        get_key = self.mov_dic_fast[key_txt]


                        if diff_x < 1.0 and diff_y < 1.0:
                            print('---- avanza slow ----')
                            get_key = self.mov_dic_slow['avanza']
                        else:
                            print('---- avanza fast ----')
                            get_key = self.mov_dic_fast['avanza']
                        
                        self.mov_msg.linear.x = get_key[0] # X
                        self.mov_msg.angular.z = get_key[1] # Z
                    
                    # si hay un objeto detente
                    else:
                        print('Hay un obstáculo enfrente')
                        print('Hacer lectura con LASER ...')
                        self.read_laser()


                self.pub.publish(self.mov_msg)
                #print(self.mov_msg) # Shown on the console
                self.rate.sleep()




# Function that initializes the node
def init_node():
    rospy.init_node('action_pub', anonymous=True)
    print('Node created successfully!')

if __name__ == '__main__':
    rospy.init_node('action_pub', anonymous=True)
    move_robot = MoveRobot(x=-2.0, y=7.0, vel_fast=1.5)
    try:
        move_robot.main() 
    except rospy.ROSInterruptException:
        pass