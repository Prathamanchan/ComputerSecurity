import cv2

camera=cv2.VideoCapture(0)

rv,image=camera.read()
del(camera)
save=raw_input("Enter Name")

cv2.imwrite(save+".png",image)

