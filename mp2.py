import cv2

cap = cv2.VideoCapture(0)#0 reserves the default web cam port and 1 for pc or external cam
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret,frame = cap.read()# so it is reading the video from the cap variable
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, ret=frame.shape

    cx = int(width/2)
    cy = int(height/2)

    pixel_center = hsv_frame[cy,cx]
    hue_value = pixel_center[0]

    color = "Undefined" #defining colours based on hue with saturation and Value set to 255)
    if hue_value <5:
        color = "RED"
    elif hue_value <22:
        color = "ORANGE"
    elif hue_value <33:
        color = "YELLOW"
    elif hue_value <43:
        color = "LIME"
    elif hue_value <33:
        color = "YELLOW"
    elif hue_value <78:
        color = "GREEN"
    elif hue_value <93:
        color = "BABY BLUE"
    elif hue_value <131:
        color = "BLUE"
    elif hue_value <140:
        color = "PURPLE"
    elif hue_value <155:
        color = "PINK"
    elif hue_value <170:
        color = "VIOLET"
    else:
        color = "RED"

    pixel_center_bgr = frame[cy,cx]    
    print(pixel_center)
    cv2.putText(frame, color, (10,50),0,1,(255,0,0), 2) # this will display the result on top left
    cv2.circle(frame,(cx,cy),5,(255,0,0),3)             # pointer in the center of the screen
    
    cv2.imshow('My Live Sketch',frame)
    if cv2.waitKey(1) == 13:
        break

cap.release() #It releases the port which was reserved
#If cap.release is not done , it might corrupt your webcam drivers
cv2.destroyAllWindows()
