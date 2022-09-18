import cv2
a = "C:/Users/DELL/Downloads/p/images (69).jfif"
img = cv2.imread(a)
imggrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face = cv2.CascadeClassifier("cascade.xml")
faces=face.detectMultiScale(img,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(250,0,0),2)
cv2.imshow("image",img)
cv2.waitKey(0)