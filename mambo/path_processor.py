#init 
from pyparrot.Minidrone import Mambo
import cv2
# If you are using BLE: you will need to change this to the address of YOUR mambo
# if you are using Wifi, this can be ignored
mamboAddr = "d0:3a:d1:dc:e6:20"

# make my mambo object
# remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
mambo = Mambo(mamboAddr, use_wifi=False)

print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

if (success):
# get the state information
	print("sleeping")
	mambo.smart_sleep(1)
	mambo.ask_for_state_update()
	mambo.smart_sleep(1)
	mambo.safe_takeoff(5)
	# take the photo
	pic_success = mambo.take_picture()
	# need to wait a bit for the photo to show up
	mambo.smart_sleep(0.5)
	picture_names = mambo.groundcam.get_groundcam_pictures_names() #get list of

	print(picture_names)
	frame = mambo.groundcam.get_groundcam_picture(picture_names[0],True) #get frame
	if frame is not None:
		if frame is not False:
			cv2.imshow("Groundcam", frame)
			cv2.waitKey(100)

	mambo.safe_land(5)
	mambo.disconnect()