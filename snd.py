from fly_tello import FlyTello

my_tellos = list()

#Tello serial number
my_tellos.append('OTQZJ96ED01TGJ')

#Use FlyTello to ensure safe landing
with FlyTello(my_tellos) as fly:
	#takeoff the drone
	fly.takeoff()
	#search_spiral(dist: int, spirals: int, height: int, speed: int, pad: str, tello: int)
	fly.search_spiral(60, 3, 40, 50, "m-2", 0)
	fly.land()
