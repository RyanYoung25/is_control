#!/usr/bin/env python
import roslib; roslib.load_manifest("is_control")
import rospy
from geometry_msgs.msg import Twist
from is_vision.msg import PioneerPos

'''
This script defines all of the pioneer motion primitives. There 
are no encoders on the robot so there is no promise on the distance
the robot will travel. The robot is able to move forward, backward, 
turn right, and turn left. Each turn is as close to 90 degrees as possible. 
Each movement is for 3 seconds
'''
forward = Twist()
forward.linear.x = .3
forward.linear.y = 0
forward.linear.z = 0
forward.angular.x = 0
forward.angular.y = 0
forward.angular.z = 0

back = Twist()
back.linear.x = -0.3
back.linear.y = 0
back.linear.z = 0
back.angular.x = 0
back.angular.y = 0
back.angular.z = 0

right = Twist()
right.linear.x = 0
right.linear.y = 0
right.linear.z = 0
right.angular.x = 0
right.angular.y = 0
right.angular.z = -0.3

left = Twist()
left.linear.x = 0
left.linear.y = 0
left.linear.z = 0
left.angular.x = 0
left.angular.y = 0
left.angular.z = 0.3

stop = Twist()
stop.linear.x = 0
stop.linear.y = 0
stop.linear.z = 0
stop.angular.x = 0
stop.angular.y = 0
stop.angular.z = 0

def turnRight(pub):
    #Do stuff now
    pub.publish(right)
    rospy.sleep(5)
    pub.publish(stop)

def goForward(pub):
    pub.publish(forward)
    rospy.sleep(3)
    pub.publish(stop)

def goBack(pub):
    pub.publish(back)
    rospy.sleep(3)
    pub.publish(stop)

def turnLeft(pub):
    pub.publish(left)
    rospy.sleep(5)
    pub.publish(stop)

def analyzeMove(data):
    #Print the data when we get it
    print data


def main():
    #Make the node so that we can publish and sleep because it takes a 
    #few seconds to get up and running
    #Advertise I am going to publish
    pub = rospy.Publisher('RosAria/cmd_vel', Twist, queue_size=10)
    rospy.init_node("pyMover", anonymous=True)
    rospy.sleep(5)

    #####Insert AI here. 

    #Subscribe to messages that the is_vision publishes
    rospy.Subscriber("robot_pos", PioneerPos, analyzeMove)

    #Drive in a square
    for i in xrange(1, 5):
        goForward(pub)
        turnRight(pub)
        

if __name__ == '__main__':
    main()

