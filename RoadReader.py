import cv2
import numpy as np

cam = cv2.VideoCapture("los_angeles.mp4")
count_line_postion = 550
min_width_react = 80
min_height_react = 80

#initialize substractor

algo = cv2.bgsegm.createBackgroundSubtractorMOG()

def center(x,y,w,h):
    x1 = int(w/2)
    y1 = int(h/2)
    cx = x+x1
    cy = y+y1
    return cy,cx

detect = []
offset = 6
counter=0

while True:  
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3),5)
    
    if ret == False:
        cam = cv2.VideoCapture("los_angeles.mp4")
        continue
    
    #apply for each frame it is convinient to use and find a spacific vehicle
    img_sub = algo.apply(blur)
    # we dilate img (dilate - expand)
    dilat = cv2.dilate(img_sub, np.ones((5,5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    dilatada = cv2.morphologyEx(dilat,cv2.MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada,cv2.MORPH_CLOSE, kernel)
    counShape, h = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.line(frame, (250,count_line_postion),(1200,count_line_postion),(0,0,0),4)
    
    for (i,c) in enumerate(counShape):
        (x,y,w,h) = cv2.boundingRect(c)
        validate_counter = (w>= min_width_react) and (h>= min_height_react)
        if not validate_counter:
            continue
        
        cv2.rectangle(frame, (x,y),(x+w, y+h),(0,0,255), 3)
    
        center2 = center(x,y,w,h)
        detect.append(center2)
        cv2.circle(frame, (center2), 5, (255,0,0),-1)
        
        for (x,y) in detect:
            if y<(count_line_postion+offset) and y>(count_line_postion-offset):
                counter+=1
            cv2.line(frame, (250,count_line_postion),(1200,count_line_postion),(0,0,0),4)
            detect.remove((x,y))
            print("vehile counter"+str(counter))
            
            
    cv2.putText(frame, 'vehile counter on street:' +str(counter),(450,70),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2, (0,255,0),5)
    
    cv2.imshow('DETECTER', dilatada)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
    cv2.imshow('Traffic', frame)
    
cam.release()
cv2.destroyAllWindows()