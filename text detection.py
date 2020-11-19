import cv2 as cv
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe"

cap = cv.VideoCapture("My movie.mp4")

counter = 0

while True:
    ret,frame = cap.read()
    counter = counter + 0.5

    if ((counter%4)==0):
        frame = cv.resize(frame,(400,400))
        w,hi,c = frame.shape
        box = pytesseract.image_to_boxes(frame)
        for b in box.splitlines():
            b = b.split()
            x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
            cv.rectangle(frame,(x,hi-y),(0+w,hi-h),(0,0,255),1)
            cv.putText(frame,b[0],(x-5,hi-y-40),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)

        cv.imshow('input',frame)
        cv.waitKey(1)