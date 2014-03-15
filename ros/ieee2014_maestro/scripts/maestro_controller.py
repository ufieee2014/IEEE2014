#!/usr/bin/env python
from __future__ import division

from ieee2014_maestro.srv import *

import rospy
import maestro
import time

class maestroController(object):
	def __init__(self):
		self.servo = None

	def change_clip_raw_position(self, req):
		self.servo.setTarget(0, req.pos)
		return ClipRawPosResponse()	

	def change_clip_position(self, clip):
		if clip.pos == 1:
			self.servo.setTarget(0,2600)
		elif clip.pos == 2:
			self.servo.setTarget(0,5700)
		elif clip.pos == 3:
			self.servo.setTarget(0,8800)
		elif clip.pos == 4:
			self.servo.setTarget(0,1000)
		elif clip.pos == 5:
			self.servo.setTarget(0,(5700+8800)//2)
		return ClipPosResponse()	

	def fire_dart(self, status):
		if status.fire == True:
			print "Fire Away!"
			self.servo.setTarget(1,6500)
			time.sleep(1)
			self.servo.setTarget(1,100)
		return FireDartResponse()
		
	def init_maestro_server(self):
		self.servo = maestro.Controller()
		rospy.init_node('maestro_server')
		test1 = rospy.Service('change_clip_position',ClipPos, self.change_clip_position)
		test2 = rospy.Service('fire_dart', FireDart, self.fire_dart)
		test3 = rospy.Service('change_clip_raw_position',ClipRawPos, self.change_clip_raw_position)
		self.servo.setTarget(1,100)
		print "Ready to go, sir!"
		rospy.spin()

test = maestroController()
test.init_maestro_server()

rospy.spin()
