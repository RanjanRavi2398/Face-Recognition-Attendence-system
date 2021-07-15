# Face-Recognition-Attendence-system
A face  recognition system is built for matching human faces with a digital image. Computer recognizes is a pixel values ranging from 0-255. In computer vision face recognition has been in since age ans has evolved over the years.  Many researchers have come up with many new techniques to efficiently identify and tell apart faces. There are many use cases such as authentication and verification of users.

#Face Recognition Library


Face recognition algorithms can extract features from a face image namely positions of forehead, eyes, nose, mouth, chin, jaws. 

Face Landmarks – There are 68 specific points (called landmarks) that exist on every face.
Face Encodings – This is the 128 encoding feature vector from a pretrained network over millions of images.
The last step is to match these encoding with the nearest possible image from a stored database.

#Steps which i have followed during building this system:


First, we get the location of where exactly the face is in the image using face_location() method(which gets the outline of the face) on the RGB image. 
Second, face encodings(markings of eyes, nose, mouth, jaws which remain the same for different images of the same person) are taken using face_encodings() function which returns a list containing 128 measurements.
Above both steps adopted for train and test images.Then a comparison between these two returned lists is done by the function compare_faces() which returns a list of boolean values(True or False). The face distance function gets the value of that by how much the two images differ. The lower the distance the better the matching and vice versa.
#Building Face Attendence System
we are ready to build a realtime face attendance system wherein webcam captured frames will be matched against the existing database images and if the match is found then it’ll store it in a CSV file called ‘Attendance Register’ along with name and time of capture. Only once the file will store the matched image’s details, if the same image is received again then it’ll not update.

#Technology

Computer Vision,Opencv, face recognition, Python



