# Drone Swarm

Code for controlling a swarm of drones, a search function, and instructions on how to set it up.

Project Overview
https://www.youtube.com/watch?v=coRY3uXSf2A

Coordinated Drone Demo
https://www.youtube.com/watch?v=YvPNt5Agnvc

Drone Search Demo
https://www.youtube.com/watch?v=ctIFRkX3dsE

1. From the wifi adapter, connect to each drone individually
2. Send router connection command to the drone
    - python3 setAP.py -s [SSID] -p [PASSWORD]
3. From the router, find the IP addresses of the drones, this changes depending on the router connected to
4. From the wifi adapter, connect to the router
5. Run scripts that use djitellopy and change IP addresses of drones accordingly in code

