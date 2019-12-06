#!/usr/bin/env python 
    
import rospy 
import time
import numpy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from ar_track_alvar_msgs.msg import AlvarMarkers
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient



soundhandle = SoundClient()
t = Twist()
linear = 0.05
angular = 0.05
lastWords = ""
listening = False
patientName = ""
birthYear1 = -1
birthYear2 = -1
birthMonth1 = -1
birthMonth2 = -1
birthDay = -1
validAnswer = False
foundMarker = ""
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
	global foundMarker
	
	while not rospy.is_shutdown():
		savedPain = "null"
		wantFood = "null"
		wantNurse = "null"
		foundMarker = "null"
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
				s = "Going to room one"
				soundhandle.say(s, voice)
				movment1 = 240
				movment2 = .75
				movment3 = -120
				movment4 = 1.5
				movment5 = -120
				movment6 = .25
				validAnswer = True

			elif("two" in lastWords):
				s = "Going to room two"
				soundhandle.say(s, voice)
				movment1 = 240
				movment2 = .75
				movment3 = -120
				movment4 = 3
				movment5 = -120
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
		s = "Hello, Nurse bot here! Please show me your patient marker"
		soundhandle.say(s, voice)
		time.sleep(2)

		foundMarker = "False"
		while(foundMarker == "False"):
			s = ""
		
		#rospy.loginfo("foundMarker - %s", foundMarker)


		#Get the patients data
		s = "Thank you, Getting your data"
		soundhandle.say(s, voice)
		time.sleep(2)
		getPatientdata()

		#Greet Patients
		s = "Hello " + patientName
		soundhandle.say(s, voice)
		time.sleep(3)
		#Start Question 1
		validAnswer = False
		while(validAnswer == False):
			s = "What is your birth year?"
			soundhandle.say(s, voice)
		
			listening = True
			while(listening):
				s = ""
				
			if(birthYear1 in lastWords or birthYear2 in lastWords):
				s = "Thank you!"
				soundhandle.say(s, voice)
				time.sleep(3)
				validAnswer = True
				
			else:
				s = "Try again, you said " + lastWords
				soundhandle.say(s, voice)
				time.sleep(3)
		
		#Start Question 2
		print("2")
		validAnswer = False
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
				s = "Try again, you said " + lastWords
				soundhandle.say(s, voice)
				time.sleep(4)

		#Start Question 3
		validAnswer = False
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
				s = "Try again, you said " + lastWords
				soundhandle.say(s, voice)

				time.sleep(3)
		
		#Start Question 4
		s = "Are you in any pain? On a scale from 0 to 10, 0 beging no pain and 10 being the worst pain ever."
		soundhandle.say(s, voice)
		time.sleep(6)
		validAnswer = False
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
				s = "Try again, you said " + lastWords
				soundhandle.say(s, voice)
				time.sleep(4)

		#Question 5
		if(savedPain == "zero" or savedPain == "one" 
		or savedPain == "two" or savedPain == "three" or savedPain == "four"):
			s = "Would you like anything to eat?"
			soundhandle.say(s, voice)
			time.sleep(6)
			validAnswer = False
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
					s = "Try again, you said " + lastWords
					soundhandle.say(s, voice)
					time.sleep(4)
			if(wantFood == "yes"):
				s = "Your options are Tuna, Pizza, Hotdog, or Salad"
				soundhandle.say(s, voice)
				time.sleep(6)
				validAnswer = False
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
						s = "Try again, you said " + lastWords
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
		validAnswer = False
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
				s = "Try again, you said " + lastWords
				soundhandle.say(s, voice)
				time.sleep(4)

		#Go back to the nurse station
		turn(-movment1)
		moveFoward(movment6)
		turn(-movment3)
		moveFoward(movment4)
		turn(-movment5)
		moveFoward(movment2)
		
		

		#Giving report
		s = "Are you ready for the report on " + patientName
		soundhandle.say(s, voice)
		time.sleep(5)
		validAnswer = False
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

		#Did the nurse hear the report?
		validAnswer = False
		while(validAnswer == False):
			s = "Did you hear the report? "
			soundhandle.say(s, voice)
			time.sleep(3)
			listening = True
			while(listening):
				s = ""
			if("no" in lastWords):
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
					if(wantFood == "no"):
						s = "The patient doesn't want any food"
						soundhandle.say(s, voice)
						time.sleep(4)
					else:
						s = "The patient would like" + wantFood
						soundhandle.say(s, voice)
						time.sleep(4)
			elif("yes" in lastWords):
				validAnswer = True
			


def getPatientdata():
	global foundMarker
	global patientName
	global birthYear1
	global birthYear2
	global birthMonth1
	global birthMonth2
	global birthDay
	if foundMarker == "1":
		patientName = "Zachary"
		birthYear1 = "nineteen ninety"
		birthYear2 = "nine"
		birthMonth1 = "june"
		birthMonth2 = "six"
		birthDay = "nineteen"
	elif foundMarker == "2":
		patientName = "Sarah"
		birthYear1 = "two thousand four"
		birthYear2 = "four"
		birthMonth1 = "september"
		birthMonth2 = "nine"
		birthDay = "seven"
	elif foundMarker == "3":
		patientName = "Bob"
		birthYear1 = "two"
		birthYear2 = "twenty sixteen"
		birthMonth1 = "febuary"
		birthMonth2 = "two"
		birthDay = "thirty"

		
	
def moveFoward(dist):
	global t
	speed = 0.25
	speedInvers = speed ** (-1)
	sleepTime = speedInvers * dist
	t.linear.x = speed
	talker(sleepTime)
	t.linear.x = 0
	time.sleep(1)




def turn(angle):
	global t
	rads = numpy.radians(angle)
	if(angle < 0):
		angSpeed = 0.5 * -1.0
	else:
		angSpeed = 0.5
	angInvers = angSpeed ** (-1)
	sleepTime = rads * angInvers
	#rospy.loginfo("Sleep time - %s", sleepTime)
	t.angular.z = angSpeed
	talker(sleepTime)
	t.angular.z = 0
	time.sleep(1)

	
	
def callback(data):           
	global lastWords
	global listening
	if(listening):	
		lastWords = data.data
		listening = False
		#rospy.loginfo("listening: %s, Hear: %s",listening,data.data) 


def talker(moveTime):     
	global t
	start = time.time()
	pub = rospy.Publisher('/mobile_base/commands/velocity', Twist,queue_size=10)
	while(((time.time() - start) < moveTime)):
		pub.publish(t)
	

def callback2(data):
	global foundMarker
	if(len(data.markers) != 0 and foundMarker == "False"):
		foundMarker = str(data.markers[0].id)
	#rospy.loginfo("Len - %s | foundMarker - %s", len(data.markers), foundMarker)


def listener():     
    rospy.init_node('listener',anonymous = False)
    rospy.Subscriber("/recognizer/output", String, callback)  	 
    rospy.Subscriber("/ar_pose_marker",AlvarMarkers,callback2)
    main()
    rospy.spin() 

if __name__ == '__main__':     
     listener() 
	 


    

    



