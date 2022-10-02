import cv2

cam = cv2.VideoCapture(0)

while True:  
    _, frame = cam.read()
    hsv_frame =cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    height, width, _ = frame.shape
    
    cx = int(width / 2)
    cy = int(height / 2)
    
    pixel_center = hsv_frame[cy,cx]
    
    hue_center = pixel_center[0]
    
    color = 'undefined'
    if hue_center < 5:
        color = 'red'
    elif hue_center < 22:
        color = 'orange'
    elif hue_center < 37:
        color = 'Lime'
    
    print(pixel_center)
    cv2.circle(frame, (cx,cy), 5, (255,0,0), 3)
    
    cv2.imshow('Roma',frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()