import cv2
import time
import numpy as np
import inmodule as htm
import math
import pycaw as py
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volrange=volume.GetVolumeRange()
#volume.SetMasterVolumeLevel(0, None)
minvol=volrange[0]
maxvol=volrange[1]


detector=htm.HandDetector(detection_con=0.7)

cap=cv2.VideoCapture(0)
ptime=0
if not cap.isOpened():
    print("Error: Could not open video capture")

print("Video capture opened successfully")
volbar=400
vol=0
volper=0


while True:
    success, img = cap.read()

    if not success:
        print("Error: Failed to capture image")
        break

    img=detector.find_hands(img)

    lmlist=detector.findpositions(img,draw=False)
    if len(lmlist)!=0:
        #print(lmlist[4],lmlist[8])

        x1,y1=lmlist[4][1],lmlist[4][2]
        x2,y2=lmlist[8][1],lmlist[8][2]
        cx,cy=(x1+x2)//2,(y1+y2)//2


        cv2.circle(img,(x1,y1),10,(255,0,255),cv2.FILLED)
        cv2.circle(img,(x2,y2),10,(255,0,255),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        cv2.circle(img,(cx,cy),10,(255,0,255),cv2.FILLED)


        length=math.hypot(x1-x2,y1-y2)
        if length<40:
            cv2.circle(img,(cx,cy),10,(0,255,0),cv2.FILLED)
        

        #hand range 30-300
        #vol range -65-0

        vol=np.interp(length,[15,300],[minvol,maxvol])
        volbar=np.interp(length,[15,300],[400,150])
        volper=np.interp(length,[15,300],[0,100])
        print(length,vol)
        volume.SetMasterVolumeLevel(vol, None)
    cv2.rectangle(img,(15,150),(85,400),(0,255,0))    
    cv2.rectangle(img,(15,int(volbar)),(85,400),(0,255,0),cv2.FILLED)    


    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(img, str(int(volper)), (40,450), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0, 0), 3)

    cv2.imshow("Hand Tracking", img)
    
    # Wait for 1 ms and check if 'q' is pressed to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

