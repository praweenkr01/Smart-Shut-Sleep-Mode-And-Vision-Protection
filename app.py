import streamlit as st
# import winsound
from faceDetectionModule import faceDetector
import cv2
import time
import os

'''this was for the beep sound'''
# from pygame import mixer
# mixer.init()
# sound=mixer.Sound("beep-21.wav")


#choosing camera...
cmno=0
for i in range(0, 5):
    cap = cv2.VideoCapture(i)
    is_camera = cap.isOpened()
    if is_camera:
        cmno=i
        cap.release()
        time.sleep(1)
        break

def func():
    prev_time=time.time()
    cap=cv2.VideoCapture(cmno)
    detector=faceDetector()
    counter=0
    z=1
    
    
    
    #check if camera working or not
    ret, frame = cap.read()
    while ret == False and z:
       if placeholder.button("Stops",key=counter):
            z=0
       counter+=1
       cap.release()
       cap = cv2.VideoCapture(cmno)                                                                              
       ret, frame = cap.read()
    
    
    
    while z:
        if placeholder.button("Stops",key=counter):
            z=0
        counter+=1
        success,img=cap.read()
#         if not success:
#             continue
        detector.findFace(img)

#         cv2.imshow('camera',detector.img)

        if detector.faces:
            prev_time=time.time()

            if detector.distance()<60:
                winsound.Beep(700, 400)
#                 print('\a')
#                 sound.play()
        else:
            temp=time.time()-prev_time
            if temp>18:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            elif temp>10:
                winsound.Beep(400, 400)
#                 print('\a')
#                 sound.play()


        cv2.waitKey(1)
        time.sleep(0.4)
        
    cap.release()
    cv2.destroyAllWindows()




st.title('Vision protector 2.0')

if st.button('Starts'):
    starter=1
    st.text('started..')
    placeholder = st.empty()
    func()
