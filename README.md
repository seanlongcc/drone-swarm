# Drone Swarm

Code for controlling a swarm of drones, a search function, and instructions on how to set it up.

Project Overview
https://www.youtube.com/watch?v=coRY3uXSf2A

Coordinated Drone Demo
https://www.youtube.com/watch?v=YvPNt5Agnvc

Dron Search Demo
https://www.youtube.com/watch?v=ctIFRkX3dsE

-From the wifi adapter, connect to each drone individually
Send router connection command to the drone
python3 setAP.py -s [SSID] -p [PASSWORD]
python3 setAP.py -s Fios-9X8ZO -p hen765cocoa9312rug
From the router, find the IP addresses of the drones, this changes depending on the router connected to, 192.168.1.1: mum95way
34:d2:62:ee:1c:5c: 192.168.1.229
34:d2:62:ee:1c:5d: 192.168.1.230
From the wifi adapter, connect to the router
Run scripts that use djitellopy and change IP addresses of drones accordingly in code
python3 (SCRIPTNAME).py
