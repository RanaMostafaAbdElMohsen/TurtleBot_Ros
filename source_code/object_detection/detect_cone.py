#!/usr/bin/env python

'''
Copyright (c) 2016, Nadya Ampilogova
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

# Script for simulation
# Launch gazebo world prior to run this script

from __future__ import print_function
import sys
import rospy
import cv2
import numpy as np
import imutils
import time
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import actionlib
from move_base_msgs.msg import MoveBaseGoal, MoveBaseAction
from actionlib_msgs.msg import GoalID

class TakePhoto:
    def __init__(self):

        self.bridge = CvBridge()
        self.image_received = False

        # Connect image topic
        img_topic = "/camera/rgb/image_raw"
        self.image_sub = rospy.Subscriber(img_topic, Image, self.callback)
        # Allow up to one second to connection
        rospy.sleep(1)

    def callback(self, data):

        # Convert image to OpenCV format
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
            return

        self.image_received = True
        self.image = cv_image
        self.detection()
        self.image_received = False
    def cancel_exploration(self):
        goal=GoalID(stamp=rospy.Time.from_sec(0.0), id="")
        explore_server.publish(goal)


    def cancel_move_base(self):
        move_base.cancel_all_goals()

    def take_picture(self, img_title):
        if self.image_received:
            # Save an image
            cv2.imwrite(img_title, self.image)
            return True
        else:
            return False

    def detection(self):
        if self.image_received:

            lowerBound=np.array([0,100,100])
            upperBound=np.array([15,255,255])

            kernelOpen=np.ones((5,5))
            kernelClose=np.ones((20,20))

            # font=cv2.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX,2,0.5,0,3,1)

            img = self.image
            img=cv2.resize(img,(340,220))

            #convert BGR to HSV
            imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
            # create the Mask
            mask=cv2.inRange(imgHSV,lowerBound,upperBound)
            #morphology
            maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
            maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

            maskFinal=maskClose
            conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

            cv2.drawContours(img,conts,-1,(255,0,0),3)

            for i in range(len(conts)):
                x,y,w,h=cv2.boundingRect(conts[i])
                rospy.loginfo("Cone found")
                self.cancel_exploration()
                self.cancel_move_base()
                #rospy.signal_shutdown("done")


if __name__ == '__main__':

    # Initialize
    rospy.init_node('take_photo', anonymous=False)
    camera = TakePhoto()
    explore_server = rospy.Publisher("/explore/cancel", GoalID,queue_size=5)
    move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)

    move_base.wait_for_server()
    rospy.spin()
