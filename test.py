from djitellopy import TelloSwarm

#scalable with more drones, just add the IP
swarm = TelloSwarm.fromIps([
    #"192.168.1.229",
    "192.168.1.230",
])

swarm.connect()
swarm.takeoff()

# run in parallel on all tellos
swarm.move_up(30)


# run by one tello after the other
#swarm.sequential(lambda i, tello: tello.move_forward(i * 40 + 100))



swarm.land()
swarm.end()
