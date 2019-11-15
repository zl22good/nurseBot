#!/usr/bin/env python 
    
import rospy 
import time
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
birthMonth = -1
birthDay = -1;
validAnswer = False;
def main():
	global lastWords
	global listening
	global soundhandle
	global patientName
	global birthYear1
	global birthYear2
	global birthMonth
	global birthDay
	global validAnswer
	print("1")
	voice = 'voice_kal_diphone'
	
	#Get the patients data
	getPatientdata();

	#Greet Patients
	s = "Hello " + patientName
    	soundhandle.say(s, voice)
	time.sleep(len(s)/4)
	#Start Question 1
	validAnswer = False;
	while(validAnswer == False):
		s = "What is your birth year?"
		soundhandle.say(s, voice)
	
		listening = True
		while(listening):
			s = ""
			
		if(lastWords == birthYear1 or lastWords == birthYear2):
			s = "Thank you!"
			soundhandle.say(s, voice)
			validAnswer = True
		else:
			s = "Try again, you said " + lastWords;
			soundhandle.say(s, voice)
			time.sleep(len(s)/6)
	
	


def getPatientdata():
	global foundMarker
	global patientName
	global birthYear1
	global birthYear2
	global birthMonth
	global birthDay
	if foundMarker == 1:
		patientName = "Zachary"
		birthYear1 = "nineteen ninety"
		birthYear2 = "nineteen ninety"
		birthMonth = "june"
		birthDay = "nineteen"

		
	

	
	
def callback(data):           
	global lastWords
	global listening

	
	if(listening):	
		lastWords = data.data
		listening = False;
	
		

		rospy.loginfo(rospy.get_caller_id()+"listening: %s, Hear: %s",listening,data.data) 


def talker():     
	pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, 	  	queue_size=10) 
     
	global t
	while not rospy.is_shutdown():

		pub.publish(t);
     	
def listener():     
     rospy.init_node('listener',anonymous = False)
     rospy.Subscriber("/recognizer/output", String, callback)     
     #talker()
     main()
     rospy.spin() 

if __name__ == '__main__':     
     listener() 


    

    


