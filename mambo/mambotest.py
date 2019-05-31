from pyparrot.Minidrone import Mambo

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
	try:
		print("sleeping")
		mambo.smart_sleep(2)
		mambo.ask_for_state_update()
		mambo.smart_sleep(2)

		print("taking off!")
		mambo.safe_takeoff(5)

		if (mambo.sensors.flying_state != "emergency"):
			print("flying state is %s" % mambo.sensors.flying_state)
			print("Rolling right")
			mambo.fly_direct(roll=20, pitch=0, yaw=0, vertical_movement=0, duration=1)
			mambo.fly_direct(roll=-20,pitch=0, yaw=0, vertical_movement=0, duration=1)

	except:
		print("can't connect, sorry!")

