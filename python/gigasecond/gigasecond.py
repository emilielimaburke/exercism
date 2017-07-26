from datetime import datetime
from datetime import timedelta

def add_gigasecond(birthdate):
	"""Calculate the moment when someone has lived for 10^9 seconds."""
	gigasecond = 10*10*10*10*10*10*10*10*10
	birthday = birthdate	
	moment = birthday + timedelta(seconds = gigasecond)
	return(moment)

