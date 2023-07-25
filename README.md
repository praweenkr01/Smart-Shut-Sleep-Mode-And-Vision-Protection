# Smart Shut/Sleep Mode And Vision Protection Features In System. [Computer Vision Project]
## Introduction
Healthy brain function needs healthy eyesight. The brain is our most vital organ, allowing us to live complex lives. Considering that our optic nerve connects our eyes and our brain, a healthy co-dependent relationship is necessary. By keeping our eyes healthy, we keep our brain healthy – improving our overall quality of life!
In this project, I have designed a few smart features using ```OpenCV, Web Camera, Streamlit & few other python module``` which can be added in our existing system as well upcoming one. **```The main motto of these features is to stop a person from watching or working by sitting too close system screen, save energy and prolong our system's life```** .

## Problem Considered
1. Sitting too close to any digital screen cause eyestrain.Children may lose interest in tasks such as reading, and old one develops irritation and tiredness.
2. Wastage of energy on forgetting to turn off the tv/laptop, no automatic brightness control feature based on making sure if person is there in frame or not & Safety of the eletronics devices(tv-laptop) from children.

## Demonstration
please do watch this short video to understand the functioning of the project.
<!-- ![Screenshot (2639)](https://user-images.githubusercontent.com/56594467/216009465-dba26c8d-b65c-4e3b-9226-482f0480107a.png) -->
[![Screenshot (2641)](https://user-images.githubusercontent.com/56594467/216013851-ce6016dc-7639-4e2d-981c-70c2421936ea.png)](https://youtu.be/R4KIiAPxklU)


## Workflow diagram
![vision_protector](https://github.com/praweenkr01/vision-protector/assets/56594467/0651044b-cbb3-4e5f-9400-938401beff6a)


## Working
The OpenCV is used to read the presense of faces after capturing with Web cam. After detecting the faces, if the person is very near to the screen the Winsound module is used to create noise,if the person doesn't backoff for too long even after warning the sysytem shutdown itself. I’ve used lens formula to know the distance between the human’s eyes and the screen  by using simlar triangles property.
If the person is working or sitting infront of the system, the system won’t go in sleepmode but as he/she moves out of frame the screen-brightness will automatically fall to lowest level,it will wait for few determined time and then start warming alarm (make beep sound) for few second and eventually go into sleepmode if no-one came in the frame. but if the person came into frame the system's brightness will be back to it's initial brightness,warning alarm will stop and system won't go into sleepmode.

### Limitation
<hr>

* won't be able to use whenever there is use of webcam in other work
* Malfunctioning of  components.
* burden of task on processor in parallel to work.
  

**Click the link below to view the ```earlier idea and implementaion``` of the same project as  ```Hardware Embedded System Project```.**<br>
<br>
[```EMBEDDED SYSTEM BASED VISION PROTECTOR```](https://praweenkr01.github.io/Smart-Shut-Sleep-Mode-And-Vision-Protection/)
