#!/usr/bin/env python
import rospy
# Brings in the SimpleActionClient
import actionlib
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from move_base_msgs.msg import MoveBaseGoal, MoveBaseAction
from actionlib_msgs.msg import GoalID
def cancel_exploration():
    goal=GoalID(stamp=rospy.Time.from_sec(0.0), id="")
    explore_server.publish(goal)


def cancel_move_base():
	move_base.cancel_all_goals()

def object_callback(object_message):
	if(object_message.data=='T'):
		cancel_exploration()
		cancel_move_base()
        rospy.signal_shutdown("done")

if __name__ == '__main__':
        rospy.init_node('listener', anonymous=True)

        rospy.Subscriber("/object", String, object_callback)
        explore_server = rospy.Publisher("/explore/cancel", GoalID,queue_size=5)
        move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)

        move_base.wait_for_server()

        rospy.spin()

    #cancel_exploration()
    #cancel_move_base()

