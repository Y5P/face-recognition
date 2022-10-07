import cv2

kamera = cv2.VideoCapture(0)

cv2.nameWindow("Python webcam")

img_counter = 0

while True:
    ret, frame = kamera.read()

    if not ret:
        print("Gagal")
        break
    
    cv2.imshow("test", frame)

    k = cv.waitKey(1)

    if k%256 == 27:
        print("Keluar")
        break

kamera.release()