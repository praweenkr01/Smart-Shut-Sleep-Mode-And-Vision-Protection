# Vision Protector(Embedded system) & Vision Protector 2.0 (computer Vision)
**Click the link below to view the ```earlier idea and implementaion``` of this project (Vision Protector) based on ```Embedded system```.**<br>
<br>
[```EMBEDDED SYSTEM BASED VISION PROTECTOR```](https://praweenkr01.github.io/vision-protector/)

## Introduction
Healthy brain function needs healthy eyesight. The brain is our most vital organ, allowing us to live complex lives. Considering that our optic nerve connects our eyes and our brain, a healthy co-dependent relationship is necessary. By keeping our eyes healthy, we keep our brain healthy – improving our overall quality of life!
In this project, I have designed a simple system called VISION PROTECTOR 2.0 using ```OpenCV, Web Camera, Streamlit & other python module``` as required in the process. **```That prevent a person from watching or working by sitting very near to system screen```** by making beep sound whenever someone come very near to tv-screen and will stop when he/she backoff.

This project solves the very basic and one of the most important and  ignored  problem.
## Problem Considered
1. Sitting too close to any digital screen cause eyestrain.Children may lose interest in tasks such as reading, and old one develops irritation and tiredness.
2. Waste of energy on forgetting to turn off the tv/laptop. & Safety of the eletronics devices(tv-laptop) from child.

## Demonstration
<!-- ![Screenshot (2639)](https://user-images.githubusercontent.com/56594467/216009465-dba26c8d-b65c-4e3b-9226-482f0480107a.png) -->
[![Screenshot (2641)](https://user-images.githubusercontent.com/56594467/216013851-ce6016dc-7639-4e2d-981c-70c2421936ea.png)](https://youtu.be/PEAq5mG8qrI)


## Workflow diagram
![taskflow](https://user-images.githubusercontent.com/56594467/216028708-9828fc33-b975-441c-851b-d736354606a4.png)

## Working
The OpenCV is used to read the presense of faces after capturing with Web cam. After detecting the faces, if the person is very near to the screen the Winsound is used to create noise till the time the person didn't backoff .I’ve used lens formula to know the distance between the human’s eyes and the screen  by using the property of light and the image formation by lens.
Till the time someone is working or sitting infront of the system, the system won’t go in sleepmode but as one moves out,it will wait for few determined time and then will give warning by making beep sound for few second and eventually go into sleepmode.
### Limitation
<hr>

* won't be able to use whenever there is use of webcam in other work
* Malfunctioning of  components.
* burden of task on processor in parallel to work.
