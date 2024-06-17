import cv2
import mediapipe as mp
import time
import inmodule as im


prev_time = 0
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video capture")

print("Video capture opened successfully")

detector = im.HandDetector()

while True:
    success, img = cap.read()
    if not success:
        print("Error: Failed to capture image")
        break

    img = detector.find_hands(img)
    landmarklist=detector.findpositions(img)
    if len(landmarklist)!=0:
        print(landmarklist)
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 255), 3)
    cv2.imshow("Hand Tracking", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()