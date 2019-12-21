import rospy
# Brings in the SimpleActionClient
import actionlib
from std_msgs.msg import Float32MultiArray
from move_base_msgs.msg import MoveBaseGoal, MoveBaseAction
from actionlib_msgs.msg import GoalID
def cancel_exploration():
    cancel_msg = GoalID(stamp=rospy.Time.from_sec(0.0), id="")
    explore_server_pub.publish(cancel_msg)


def cancel_move_base():
	move_base.cancel_goal()

def object_callback(object_message):
	if(object_message.size()>0):
		cancel_exploration()
		cancel_move_base()

if __name__ == '__main__':
	rospy.init_node('node', anonymous=True)

    #rospy.Subscriber("/object", Float32MultiArray, object_callback)#listen to object detection module
	move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
	move_base.wait_for_server()
	explore_server_pub = rospy.Publisher("/explore_server/cancel", GoalID)
    #rospy.sleep(500)
    cancel_exploration()
	cancel_move_base()
