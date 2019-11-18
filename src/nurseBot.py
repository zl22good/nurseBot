#!/usr/bin/env python 
    
import rospy 
import time
import numpy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient


linear = 0.05;
angular = 0.05;
soundhandle = SoundClient();
t = Twist();
lastWords = "";
listening = False;
foundMarker = 1;
patientName = "";
birthYear1 = -1;
birthYear2 = -1;
birthMonth1 = -1;
birthMonth2 = -1;
birthDay = -1;
validAnswer = False;
def main():
	global lastWords
	global listening
	global soundhandle
	global patientName
	global birthYear1
	global birthYear2
	global birthMonth1
	global birthMonth2
	global birthDay
	global validAnswer
	

	savedPain = "null"
	wantFood = "null"
	wantNuse = "null"
	voice = 'voice_kal_diphone'
	
	#Wait for nurse to tell which room to see
	validAnswer = False
	while(validAnswer == False):
		s = "Which room would you like me to check?"
		soundhandle.say(s, voice)
	
		listening = True
		while(listening):
			s = ""

		if("one" in lastWords):
			movment1 = 180
			movment2 = .5
			movment3 = 90
			movment4 = 1
			movment5 = 90
			movment6 = .25
			validAnswer = True

		elif("two" in lastWords):
			movment1 = 180
			movment2 = .5
			movment3 = 90
			movment4 = 2
			movment5 = -90
			movment6 = .25
			validAnswer = True

	#Move to that patient
	turn(movment1)
	moveFoward(movment2)
	turn(movment3)
	moveFoward(movment4)
	turn(movment5)
	moveFoward(movment6)

	#Scan ar code

	#Get the patients data
	getPatientdata();

	#Greet Patients
	s = "Hello " + patientName
	soundhandle.say(s, voice);
	time.sleep(3)
	#Start Question 1
	validAnswer = False;
	while(validAnswer == False):
		s = "What is your birth year?"
		soundhandle.say(s, voice)
	
		listening = True
		while(listening):
			s = ""
			
		if(birthYear1 in lastWords or birthYear2 in lastWords):
			s = "Thank you!"
			print("3")

			soundhandle.say(s, voice)
			print("3")

			time.sleep(3)
			print("3")
			validAnswer = True
			print("3")
		else:
			s = "Try again, you said " + lastWords;
			soundhandle.say(s, voice)
			time.sleep(3)
	
	#Start Question 2
	print("2")
	validAnswer = False;
	while(validAnswer == False):
		s = "What is your birth month?"
		soundhandle.say(s, voice)
	
		listening = True
		while(listening):
			s = ""
			
		if(birthMonth1 in lastWords or birthMonth2 in lastWords):
			s = "Thank you!"
			soundhandle.say(s, voice)
			time.sleep(3)
			validAnswer = True
		else:
			s = "Try again, you said " + lastWords;
			soundhandle.say(s, voice)
			time.sleep(4)

	#Start Question 3
	validAnswer = False;
	while(validAnswer == False):
		s = "What is your birth day?"
		soundhandle.say(s, voice)
	
		listening = True
		while(listening):
			s = ""
			
		if(birthDay in lastWords):
			s = "Thank you! Identity Confrimed!"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
			print("3")
		else:
			s = "Try again, you said " + lastWords;
			soundhandle.say(s, voice)

			time.sleep(3)
	
	#Start Question 2
	print("2")
	validAnswer = False;
	while(validAnswer == False):
		s = "What is your birth month?"
		soundhandle.say(s, voice)
	
		listening = True
		while(listening):
			s = ""
			
		if(birthMonth1 in lastWords or birthMonth2 in lastWords):
			s = "Thank you!"
			soundhandle.say(s, voice)
			time.sleep(3)
			validAnswer = True
		else:
			s = "Try again, you said " + lastWords;
			soundhandle.say(s, voice)
			time.sleep(4)

	#Start Question 3
	validAnswer = False;
	while(validAnswer == False):
		s = "What is your birth day?"
		soundhandle.say(s, voice)
	
		listening = True
		while(listening):
			s = ""
			
		if(birthDay in lastWords):
			s = "Thank you! Identity Confrimed!"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		else:
			s = "Try again, you said " + lastWords;
			soundhandle.say(s, voice)
			time.sleep(4)
	
	#Start Question 4
	s = "Are you in any pain? On a scale from 0 to 10, 0 beging no pain and 10 being the worst pain ever."
	soundhandle.say(s, voice)
	time.sleep(6)
	validAnswer = False;
	while(validAnswer == False):
			
		listening = True
		while(listening):
			s = ""
			
		if("zero" in lastWords):
			savedPain = "zero"
			s = "Good, your pain is low today!"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("one" in lastWords):
			savedPain = "one"
			s = "Good, your pain is low today!"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("two" in lastWords):
			savedPain = "two"
			s = "Good, your pain is low today!"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("three" in lastWords):
			savedPain = "three"
			s = "Good, your pain is low today!"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("four" in lastWords):
			savedPain = "four"
			s = "Good, your pain is low today!"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("five" in lastWords):
			savedPain = "five"
			s = "Oh no your pain is high today! We will tell the nurse"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("six" in lastWords):
			savedPain = "six"
			s = "Oh no your pain is high today! We will tell the nurse"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("seven" in lastWords):
			savedPain = "seven"
			s = "Oh no your pain is high today! We will tell the nurse"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("eight" in lastWords):
			savedPain = "eight"
			s = "Oh no your pain is high today! We will tell the nurse"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("nine" in lastWords):
			savedPain = "nine"
			s = "Oh no your pain is high today! We will tell the nurse"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("ten" in lastWords):
			savedPain = "ten"
			s = "Oh no your pain is high today! We will tell the nurse"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		else:
			s = "Try again, you said " + lastWords;
			soundhandle.say(s, voice)
			time.sleep(4)

	#Question 5
	if(savedPain == "zero" or savedPain == "one" 
	or savedPain == "two" or savedPain == "three" or savedPain == "four"):
		s = "Would you like anything to eat?"
		soundhandle.say(s, voice)
		time.sleep(6)
		validAnswer = False;
		while(validAnswer == False):
			listening = True
			while(listening):
				s = ""
			if("yes" in lastWords):
				wantFood = "yes"
				validAnswer = True
			elif("no" in lastWords):
				wantFood = "no"
				validAnswer = True
			else:
				s = "Try again, you said " + lastWords;
				soundhandle.say(s, voice)
				time.sleep(4)
		if(wantFood == "yes"):
			s = "Your options are Tuna, Pizza, Salad, or Hotdog"
			soundhandle.say(s, voice)
			time.sleep(6)
			validAnswer = False;
			while(validAnswer == False):
				s = "Please state your option"
				soundhandle.say(s, voice)
				time.sleep(5)
				listening = True
				while(listening):
					s = ""
				if("tuna" in lastWords):
					wantFood = "tuna"
					validAnswer = True
				elif("pizza" in lastWords):
					wantFood = "pizza"
					validAnswer = True
				elif("salad" in lastWords):
					wantFood = "salad"
					validAnswer = True
				elif("hotdog" in lastWords):
					wantFood = "hotdog"
					validAnswer = True
				else:
					s = "Try again, you said " + lastWords;
					soundhandle.say(s, voice)
					time.sleep(4)
					s = "Do you need the food options again?"
					soundhandle.say(s, voice)
					time.sleep(4)
					while(validAnswer == False):
						listening = True
						while(listening):
							s = ""
						if("yes" in lastWords):
							s = "Your options are Tuna, Pizza, Salad, or Hotdog"
							soundhandle.say(s, voice)
							time.sleep(5)
							validAnswer = True
						elif("no" in lastWords):
							validAnswer = True
					validAnswer = False

	#Question 6
	s = "Do you need the nurse?"
	soundhandle.say(s, voice)
	time.sleep(4)
	validAnswer = False;
	while(validAnswer == False):
		listening = True
		while(listening):
			s = ""
		if("yes" in lastWords):
			wantNurse = "yes"
			s = "Okay, well let the nurse know. Hope you fell better"
			soundhandle.say(s, voice)
			time.sleep(5)
			validAnswer = True
		elif("no" in lastWords):
			wantNurse = "no"
			s = "Okay, have a great day"
			soundhandle.say(s, voice)
			time.sleep(3)
			validAnswer = True
		else:
			s = "Try again, you said " + lastWords;
			soundhandle.say(s, voice)
			time.sleep(4)
	
	#Start Question 4
	s = "Are you in any pain? On a scale from 0 to 10, 0 beging no pain and 10 being the worst pain ever."
	soundhandle.say(s, voice)
	time.sleep(6)
	validAnswer = False;
	while(validAnswer == False):
			
		listening = True
		while(listening):
			s = ""
			
		if("zero" in lastWords):
			savedPain = "zero"
			s = "Good, your pain is low today!"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("one" in lastWords):
			savedPain = "one"
			s = "Good, your pain is low today!"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("two" in lastWords):
			savedPain = "two"
			s = "Good, your pain is low today!"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("three" in lastWords):
			savedPain = "three"
			s = "Good, your pain is low today!"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("four" in lastWords):
			savedPain = "four"
			s = "Good, your pain is low today!"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("five" in lastWords):
			savedPain = "five"
			s = "Oh no your pain is high today! We will tell the nurse"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("six" in lastWords):
			savedPain = "six"
			s = "Oh no your pain is high today! We will tell the nurse"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("seven" in lastWords):
			savedPain = "seven"
			s = "Oh no your pain is high today! We will tell the nurse"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("eight" in lastWords):
			savedPain = "eight"
			s = "Oh no your pain is high today! We will tell the nurse"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("nine" in lastWords):
			savedPain = "nine"
			s = "Oh no your pain is high today! We will tell the nurse"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		elif("ten" in lastWords):
			savedPain = "ten"
			s = "Oh no your pain is high today! We will tell the nurse"
			soundhandle.say(s, voice)
			time.sleep(4)
			validAnswer = True
		else:
			s = "Try again, you said " + lastWords;
			soundhandle.say(s, voice)
			time.sleep(4)

	#Question 5
	if(savedPain == "zero" or savedPain == "one" 
	or savedPain == "two" or savedPain == "three" or savedPain == "four"):
		s = "Would you like anything to eat?"
		soundhandle.say(s, voice)
		time.sleep(6)
		validAnswer = False;
		while(validAnswer == False):
			listening = True
			while(listening):
				s = ""
			if("yes" in lastWords):
				wantFood = "yes"
				validAnswer = True
			elif("no" in lastWords):
				wantFood = "no"
				validAnswer = True
			else:
				s = "Try again, you said " + lastWords;
				soundhandle.say(s, voice)
				time.sleep(4)
		if(wantFood == "yes"):
			s = "Your options are Tuna, Pizza, Salad, or Hotdog"
			soundhandle.say(s, voice)
			time.sleep(6)
			validAnswer = False;
			while(validAnswer == False):
				s = "Please state your option"
				soundhandle.say(s, voice)
				time.sleep(5)
				listening = True
				while(listening):
					s = ""
				if("tuna" in lastWords):
					wantFood = "tuna"
					validAnswer = True
				elif("pizza" in lastWords):
					wantFood = "pizza"
					validAnswer = True
				elif("salad" in lastWords):
					wantFood = "salad"
					validAnswer = True
				elif("hotdog" in lastWords):
					wantFood = "hotdog"
					validAnswer = True
				else:
					s = "Try again, you said " + lastWords;
					soundhandle.say(s, voice)
					time.sleep(4)
					s = "Do you need the food options again?"
					soundhandle.say(s, voice)
					time.sleep(4)
					while(validAnswer == False):
						listening = True
						while(listening):
							s = ""
						if("yes" in lastWords):
							s = "Your options are Tuna, Pizza, Salad, or Hotdog"
							soundhandle.say(s, voice)
							time.sleep(5)
							validAnswer = True
						elif("no" in lastWords):
							validAnswer = True
					validAnswer = False

	#Question 6
	s = "Do you need the nurse?"
	soundhandle.say(s, voice)
	time.sleep(4)
	validAnswer = False;
	while(validAnswer == False):
		listening = True
		while(listening):
			s = ""
		if("yes" in lastWords):
			wantNurse = "yes"
			s = "Okay, well let the nurse know. Hope you fell better"
			soundhandle.say(s, voice)
			time.sleep(5)
			validAnswer = True
		elif("no" in lastWords):
			wantNurse = "no"
			s = "Okay, have a great day"
			soundhandle.say(s, voice)
			time.sleep(3)
			validAnswer = True
		else:
			s = "Try again, you said " + lastWords;
			soundhandle.say(s, voice)
			time.sleep(4)


	#Go back to the nurse station
	turn(movment1)
	moveFoward(movment6)
	turn(-movment5)
	moveFoward(movment4)
	turn(-movment3)
	moveFoward(movment2)
	
	

	#Giving report
	s = "Are you ready for the report on " + patientName
	soundhandle.say(s, voice)
	time.sleep(5)
	validAnswer = False;
	while(validAnswer == False):
		listening = True
		while(listening):
			s = ""
		if("yes" in lastWords):
			validAnswer = True

	

	s = "The patients pain level is " + savedPain
	soundhandle.say(s, voice)
	time.sleep(4)
	if(wantNurse == "yes"):
		s = "The patient would like to see you"
		soundhandle.say(s, voice)
		time.sleep(4)
	else:
		s = "The patient doesn't need to see you"
		soundhandle.say(s, voice)
		time.sleep(4)
	if(wantFood != "null"):
		if(wantNurse == "no"):
			s = "The patient doesn't want any food"
			soundhandle.say(s, voice)
			time.sleep(4)
		else:
			s = "The patient would like" + wantFood
			soundhandle.say(s, voice)
			time.sleep(4)
			


def getPatientdata():
	global foundMarker
	global patientName
	global birthYear1
	global birthYear2
	global birthMonth1
	global birthMonth2
	global birthDay
	if foundMarker == 1:
		patientName = "Zachary"
		birthYear1 = "nineteen ninety"
		birthYear2 = "nineteen ninety"
		birthMonth1 = "june"
		birthMonth2 = "six"
		birthDay = "nineteen"

		
	
def moveFoward(dist):
	global t
	speed = 0.25
	speedInvers = speed ** (-1)
	sleepTime = speedInvers * dist
	t.linear.x = speed
	time.sleep(sleepTime)
	t.linear.z = 0




def turn(angle):
	global t
	rads = numpy.radians(angle)
	angSpeed = 0.5
	angInvers = angSpeed ** (-1)
	sleepTime = rads * angInvers;
	t.angular.z = angSpeed
	rospy.loginfo("t.angular.z: %s, sleepTime: %s",t.angular.z,sleepTime) 
	time.sleep(sleepTime)
	rospy.loginfo("sleepTime: %s",sleepTime) 
	t.angular.z = 0

	
	
def callback(data):           
	global lastWords
	global listening

	
	if(listening):	
		lastWords = data.data
		listening = False;
	
		

		rospy.loginfo("listening: %s, Hear: %s",listening,data.data) 


def talker():     
	pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, 	  	queue_size=10) 
     
	global t
	while not rospy.is_shutdown():

		pub.publish(t);
     	
def listener():     
     rospy.init_node('listener',anonymous = False)
     rospy.Subscriber("/recognizer/output", String, callback)     
     main()
     rospy.spin() 

if __name__ == '__main__':     
     listener() 
	 talker()


    

    



