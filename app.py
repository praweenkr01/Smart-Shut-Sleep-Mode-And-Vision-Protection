import streamlit as st
import winsound
from faceDetectionModule import faceDetector
import cv2
import time
import os
import screen_brightness_control as sbc



# this was for the beep sound
# from pygame import mixer
# mixer.init()
# sound=mixer.Sound("beep-21.wav")


#choosing camera...
cmno=0 #camera number...in use
for i in range(0, 5):
    cap = cv2.VideoCapture(i)
    is_camera = cap.isOpened()
    if is_camera:
        cmno=i
        cap.release()
        time.sleep(1)
        break

# this func carry out all the possible logic within it 
# we just need to call this whenever we wish to use this feature in out system

def func():

    # taking acoount of last time when there was someone infront of camera
    prev_time=time.time()
    # capture
    cap=cv2.VideoCapture(cmno)

    # making an object detector by instantiating faceDetector
    detector=faceDetector()

    # counter for inplace stop button in streamlit
    counter=0
    # this z for looping in while
    z=1
    
    
    
    #check if camera working or not
    # ret, frame = cap.read()
    # while ret == False and z:
    #    if placeholder.button("Stops",key=counter):
    #         z=0
    #    counter+=1
    #    cap.release()
    #    cap = cv2.VideoCapture(cmno)                                                                              
    #    ret, frame = cap.read()

    
    close_shut=0 #this keep account of for how log the person is too close to screen
    target=sbc.get_brightness() #taking note of initial brightness of sysytem
    vol=target[0] #this variable will be used to control brightness
    

    while z:

        # stop button appear so that one can off this feature
        if placeholder.button("Stops",key=counter):
            z=0

        success,img=cap.read()
        # if not success:
        #     continue

        detector.findFace(img)
        # cv2.imshow('camera',detector.img)

        # if person is infront of system
        if detector.faces:
            
            # if brightness is not as it was initially
            # change that to as it was 
            if vol!=target[0]:
                vol=target[0]
                sbc.set_brightness(vol)


            # updating the last time person was infront
            prev_time=time.time()

            # if person is too close to screen
            if detector.distance()<60:

                # make beep sound
                winsound.Beep(700, 400)
                close_shut+=1

                # if the person is too close to screen for long time
                if close_shut>15:
                    # shutdown the sysytem
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            else:
                close_shut=0

        # there is no one infront
        else:

            # make brightness 0(lowest)
            if vol!=0:
                vol=0
                sbc.set_brightness(vol)

            # check for how long there is no one infront
            temp=time.time()-prev_time

            # if there is noone for long time
            if temp>18:
                # shutdown
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            # give warning for few sec before shutdown
            elif temp>10:
                winsound.Beep(400, 400)

        # cv2.waitKey(1)
        counter+=1
        time.sleep(0.4)
        
    cap.release()
    cv2.destroyAllWindows()




#Title of project to be displayed
st.title('Smart Shut/sleep mode and vision protection in system')

# the start button
if st.button('Starts'):
    starter=1
    st.text('started..')
    placeholder = st.empty()
    func()