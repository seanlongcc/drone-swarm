from djitellopy import TelloSwarm

#drone 1 left, drone 2 right
swarm = TelloSwarm.fromIps([
    "192.168.1.229",
    "192.168.1.230",
])

swarm.connect()
swarm.takeoff()

#swarm circle
swarm.move_up(50)
swarm.curve_xyz_speed(0,-60,180,0,-60,20,60)

#sequentially move forward
swarm.sequential(lambda i, tello: tello.move_forward(100))

#face eachother
i = 0
for tello in swarm:
	print(tello)
	#first drone
	if i == 0:
		i+=1
		tello.rotate_clockwise(90)
		continue
	#second drone
	tello.rotate_counter_clockwise(90)
	
#flip backward
swarm.flip('r')

#switch spots
swarm.curve_xyz_speed(60,20,0,60,180,0,60)

#rotate and face eachother again
i = 0
for tello in swarm:
	#first drone
	if i == 0:
		i+=1
		tello.rotate_clockwise(90)
		continue
	#second drone
	tello.rotate_clockwise(90)
	
#move forward
swarm.move_forward(100)

#spin in place
swarm.rotate_clockwise(360)

#land
swarm.land()
swarm.end()
