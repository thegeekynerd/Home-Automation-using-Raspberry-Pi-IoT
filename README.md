# Home Automation

Uses Raspberry Pi 3b+

Pins to be used(in BCM mode):
Appliance1 : 3
Appliance2 : 4
Appliance3 : 17
Appliance4 : 27
Appliance5 : 22

Routes:
/switch : for controlling the Appliances from one page
/action<number> : number ranges from 1 to 5, request for direct appliance control
/status : Get status information on appliances, on or off, along with total running time (running streak to be added)
