#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import sys, select, termios, tty
import geometry_msgs
import nav_msgs
def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key
#init ros things
rospy.init_node('test')
fl_pub = rospy.Publisher("front_left", Float32)
fr_pub = rospy.Publisher("front_right", Float32)
bl_pub = rospy.Publisher("back_left", Float32)
br_pub = rospy.Publisher("back_right", Float32)
cmd_vel = rospy.Publisher("cmd_vel", geometry_msgs.msg.Twist)
yaw = rospy.Subscriber("odom",nav_msgs.msg.Odometry,set_yaw)

r = rospy.Rate(50)
c = 0
settings = termios.tcgetattr(sys.stdin)

yaw = 0

def set_yaw(msg):
    pass

while not rospy.is_shutdown():
    try:
        key = getKey()
        print("key:  ",key)
    except:
        key = 100
    option = int(c/100)
    # move forward
    if key == 'w':
        fl_pub.publish(1.0)
        fr_pub.publish(1.0)
        bl_pub.publish(1.0)
        br_pub.publish(1.0)
    # move back
    if key == 's':
        fl_pub.publish(-1.0)
        fr_pub.publish(-1.0)
        bl_pub.publish(-1.0)
        br_pub.publish(-1.0)

    # move left
    if key == 'a':
        fl_pub.publish(-1.0)
        fr_pub.publish(1.0)
        bl_pub.publish(1.0)
        br_pub.publish(-1.0)

    # move right
    if key == 'd':
        fl_pub.publish(1.0)
        fr_pub.publish(-1.0)
        bl_pub.publish(-1.0)
        br_pub.publish(1.0)

    # spin
    if key == 'g':
        fl_pub.publish(-1.0)
        fr_pub.publish(1.0)
        bl_pub.publish(-1.0)
        br_pub.publish(1.0)

    # spin
    if key == 'h':
        fl_pub.publish(1.0)
        fr_pub.publish(-1.0)
        bl_pub.publish(1.0)
        br_pub.publish(-1.0)
    if key == 'q':
        break
    if key == 't':
        fl_pub.publish(0.0)
        fr_pub.publish(0.0)
        bl_pub.publish(0.0)
        br_pub.publish(0.0)

    c += 1
    if c > 600:
        c = 0

    r.sleep()
