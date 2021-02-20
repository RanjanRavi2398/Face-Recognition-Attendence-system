import cv2
import numpy as np
import face_recognition

imgAndrew=face_recognition.load_image_file('Attendence_FaceRecognition_Project/Images/Andrew_Ng.png')
imgAndrew=cv2.cvtColor(imgAndrew,cv2.COLOR_BGR2RGB)
imgTest=face_recognition.load_image_file('Attendence_FaceRecognition_Project/Test_Images/Andrew_test.jfif')
imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc=face_recognition.face_locations(imgAndrew)[0]
encodeAndrew=face_recognition.face_encodings(imgAndrew)[0]
cv2.rectangle(imgAndrew,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,255,0),2)
facetestLoc=face_recognition.face_locations(imgTest)[0]
encodeTest=face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(facetestLoc[3],facetestLoc[0]),(facetestLoc[1],facetestLoc[2]),(255,255,0),2)

results=face_recognition.compare_faces([encodeAndrew],encodeTest)
faceDis=face_recognition.face_distance([encodeAndrew],encodeTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results}{round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
cv2.imshow('Andrew_Ng',imgAndrew)
cv2.imshow('Andrew_test',imgTest)
cv2.waitKey(0)