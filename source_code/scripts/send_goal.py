#!/usr/bin/env python
from move_base_msgs.msg import MoveBaseGoal, MoveBaseAction
import rospy
import sys
import actionlib
from tf.transformations import quaternion_from_euler, euler_from_quaternion

if __name__ == '__main__':
        rospy.init_node('node', anonymous=True)
        move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        move_base.wait_for_server()
        goal=MoveBaseGoal()
        x_target=float(sys.argv[1])
        y_target=float(sys.argv[2])
        theta_target=float(sys.argv[3])

        quat = quaternion_from_euler(0, 0, theta_target)

        goal.target_pose.header.stamp = rospy.get_rostime()
        goal.target_pose.header.frame_id = '/map' # Note: the frame_id must be map
        goal.target_pose.pose.position.x = x_target
        goal.target_pose.pose.position.y = y_target
        goal.target_pose.pose.position.z=0.0

        goal.target_pose.pose.orientation.x = quat[0]
        goal.target_pose.pose.orientation.y = quat[1]
        goal.target_pose.pose.orientation.z = quat[2]
        goal.target_pose.pose.orientation.w = quat[3]
        move_base.send_goal(goal)

