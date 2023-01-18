import streamlit as st
# import winsound
from faceDetectionModule import faceDetector
import cv2
import time
import os
# from pygame import mixer
# mixer.init()
# sound=mixer.Sound("beep-21.wav")


def func():
    prev_time=time.time()
    cap=cv2.VideoCapture(0)
    detector=faceDetector()
    counter=0
    z=1
    while z:
        if placeholder.button("Stops",key=counter):
            z=0
        counter+=1
        success,img=cap.read()
        if not success:
            continue
        detector.findFace(img)

#         cv2.imshow('camera',detector.img)

        if detector.faces:
            prev_time=time.time()

            if detector.distance()<60:
                print('\a')
#                 sound.play()
        else:
            temp=time.time()-prev_time
            if temp>18:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            elif temp>10:
                print('\a')
#                 sound.play()


        cv2.waitKey(1)
        
        time.sleep(0.2)
    cap.release()
    cv2.destroyAllWindows()




st.title('Vision protector 2.0')

if st.button('Starts'):
    starter=1
    st.text('started..')
    placeholder = st.empty()
    func()
