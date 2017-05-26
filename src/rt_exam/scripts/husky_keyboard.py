#!/usr/bin/env python
import roslib
import rospy

from geometry_msgs.msg import Twist

import sys, select, termios, tty

msg = """
Reading from the keyboard
---------------------------
Moving around:
W = front move
S = back move

CTRL-C to quit
"""
def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	return key

if __name__=="__main__":
    	settings = termios.tcgetattr(sys.stdin)
	
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
	rospy.init_node('husky_keyboard')

	speed = 2
	x = 0

	try:
		print msg
		while(1):
			key = getKey()
			if (key == 'w'):
				x = 2
			elif (key == 's'):
				x = -2
			else:
				break

			twist = Twist()
			twist.linear.x = x*speed;
			pub.publish(twist)

	finally:
		twist = Twist()
		twist.linear.x = x*speed;
		pub.publish(twist)




