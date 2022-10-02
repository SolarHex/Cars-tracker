import cv2
import numpy as np    

cam = cv2.VideoCapture(0)
lines = 250
counter = 0

while True:  
    _, frame = cam.read()
    
    
    cv2.line(frame, (50,lines), (575,lines), (255,0,0), 3)
    
    cv2.circle(frame, (50,450),2,(0,255,0),-1)
    cv2.circle(frame, (50,300),2,(0,255,0),-1)
    cv2.circle(frame, (575,450),2,(0,255,0),-1)
    cv2.circle(frame, (575,300),2,(0,255,0),-1)
    
    pts1 = np.float32([[50,450],[50,300],[575,450],[575,300]])
    pts2 = np.float32([[0,0],[400,0],[0,600],[400,600]])
    
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    result = cv2.warpPerspective(frame,matrix,(400,600))
    
    if _ in result:
        counter+=1
    
    cv2.putText(frame, "AMOUNT OF CARS:"+str(counter),(25,70),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1, (0,255,0),5)
    
    cv2.imshow('pop',frame)
   #cv2.imshow('road',result)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()