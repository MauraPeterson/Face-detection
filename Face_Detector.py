"""
Code from: https://youtu.be/XIrOM9oP3pA

import cv2

#Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml;)

# Choose an image to detect faces in
img = cv2.imread('RDJ.png')
#img = cv2.imread('JT.jpg')

# Must convert to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# Draw rectangles around the faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the image with the faces spotted
cv2.imshow('Clever Programmer Face Detector', img)

#Wait here in the code and listen for a key press
cv2.waitKey()
"""

import cv2

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
#img = cv2.imread('lady.png')

# To capture video from webcam
webcam = cv2.VideoCapture(0)

# Iterate forever over frames
while True:
        # Read the current frame
        successful_frame_read, frame = webcam.read()

        # Must conver to grayscale
        grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

        # Draw rectangles around the faces
        for (x, y, w, h) in face_coordinates:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

        # Show images
        cv2.imshow('Clever Programmer Face Detector', frame)


        # Wait 1ms and listen for a key press
        cv2.waitKey(1)

# Must conver to grayscale
#grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
#face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# Draw rectangles around the faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

# manually draw rectangle with the coordinates for lady.png
# cv2.rectangle(img, (107, 44), (938 + 107, 938 + 44), (0, 255, 0), 2)

# Print coordinates
# print(face_coordinates)

#cv2.imshow('Clever Programmer Face Detector', img)


# Wait here in the code and listen for a key press
#cv2.waitKey()

print("Code Completed")