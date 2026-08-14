import cv2

def capture_photo():
    cam = cv2.VideoCapture(0)
        
    if not cam.isOpened():
        print("Error: Could not open the camera.")
        exit()
        
    ret, frame = cam.read()
    if ret:
        cv2.imwrite("images/capture.jpg", frame)
        print("Photo saved successfully as 'photo.jpg'")
    else:
        print("Error: Could not read a frame from the camera.")
        
    cam.release()
    cv2.destroyAllWindows()

