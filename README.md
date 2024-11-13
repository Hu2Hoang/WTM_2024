# Sky Helper
## _Solution for finding lost person according to wifi probe_
 
## Methodology
According to Statista, the current number of smartphone users in the world is 6.648 billion people, equivalent to 83.72% of the world population owning smartphones. Really few people turn off wifi feature. So we do not track missing people directly, but through smartphones or laptops or wearable devices such as: Apple Watch, headphone, ...
 
### Wifi Probe Frames
Wi-Fi devices are continually emitting "probe frames," calling out for nearby Wi-Fi networks to connect to. In order to function, Wi-Fi devices are always doing one of two things to try to discover available networks; They either send out beacon frames or probe frames. The second way a Wi-Fi connection happens is when your device attempts to find a nearby network to connect to by sending out a kind of packet called a probe frame.
 
### Tracking Wi-Fi Devices via Probe Frames
Using probe frames and the ability to decloak or track users, we can learn a lot of information. Besides being able to detect intruders in areas they're not supposed to be, we're also able to monitor human activity and keep track of when people come and go. We can see what networks people have permission to connect to, and with multiple Wi-Fi sensors, we can track their movement in real time. Major retailers use this practice to monitor customer traffic flow through stores, using it to sell the retail space customers spend the most time to manufacturers at a premium.
 
## Problem
For accurate calculation, 3 positions of the drone are required and the distance from the missing person to the drone, the problem returns: find the vertex of a quadrilateral when knowing 3 vertices and the distance from the missing vertex to 3 remain vertices.
 
## Manual Guide
### On Raspberry Pi
Step 1: Make sure you have a wireless network card that support monitor mode
<br>
Step 2: Clone the repository
```
git clone https://github.com/Hu2Hoang/GSC_2023.git
cd GSC_2023
```
Step 3: Run two command bellow parallely
```
sudo python3 locate_def.py
```
![](https://i.imgur.com/tooTbT0.png "")
<br>
Three paramaters display on the screen are
* MAC Address
* RSSI
* The distance to the flycam
 
```
sudo python3 firebase_gps.py
```
![](https://i.imgur.com/YuBNMZj.png "")
Three paramaters display on the screen are
* latitude
* longitude
* height
 
### On Android
Download the .apk file at [link](https://github.com/Hu2Hoang/GSC_2023/blob/main/ptitgsc2/app/release/app-release.apk).
The main Interface
* Part 1: The map view
![](https://i.imgur.com/exUFLwl.jpg "")
When you press into a specific point at the map, you can see the MAC Address of the device for marking easier
 
* Part 2: Stream camera from fly cam
<br>
The RTSP Server is hosted on Google Cloud
<br>
 
![](https://i.imgur.com/0uBQPaI.jpg "")
 
The realtime image
 
![](https://i.imgur.com/JyWqewm.jpg "")
 
* Part 3: Two button
![](https://i.imgur.com/vPWuwde.jpg "")
* Update: When flycam move to the location that you want (You can decide through the GPS and the realtime image). You can press "Update" for save the recent location of flycam. You must have to update 3 times to have the data to calculate the most complete
* Reset: Delete all saved data to start a new session
