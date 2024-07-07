import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.

abhi = face_recognition.load_image_file("attendance/photo/7. Abhishek.jpg")
abhi_face_encoding = face_recognition.face_encodings(abhi)[0]

# Load a second sample picture and learn how to recognize it.
Avi = face_recognition.load_image_file("attendance/photo/5.Avinash.jpg")
Avi_face_encoding = face_recognition.face_encodings(Avi)[0]

seja = face_recognition.load_image_file("attendance/photo/6.Sejal.jpg")
seja_face_encoding = face_recognition.face_encodings(seja)[0]

vaishnavi = face_recognition.load_image_file("attendance/photo/8. vaishnavi.jpg")
vaishnavi_face_encoding = face_recognition.face_encodings(vaishnavi)[0]

# Create arrays of known face encodings and their names
#encoding means  the process of changing the format of content for optimal transmission or storage
known_face_encodings = [
    abhi_face_encoding,
    Avi_face_encoding,
    seja_face_encoding ,
    vaishnavi_face_encoding 

]
known_face_names = [
    "7. Abhishek ",
    "5. Avinash",
    "6.Sejal",
    "8.Vaishnavi"
    
]

students = known_face_names.copy()

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

def mark(name):
    with open(current_date+'.csv','a+',newline='') as f:
        lnwriter = csv.writer(f)
        current_time = now.strftime("%H-%M-%S")
        lnwriter.writerow([name,current_time])


while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame =cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)                 #a pre-defined method used to add a single item to certain collection types
            if name in known_face_names:
                if name in students:
                    students.remove(name)
                  
                    mark(name)
            

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()