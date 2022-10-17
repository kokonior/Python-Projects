#program ip cctv
import cv2 as cv
wifiCamera = cv.VideoCapture('http:192.168.1.19:8080/video')
while(True):
    ret, frame = wifiCamera.read() 
    cv.imshow('Tampilkan Wifi',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
wifiCamera.release()
cv.destroyAllWindows()
