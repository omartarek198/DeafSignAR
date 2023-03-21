import tracker
import classifier
import client
# import bluetoothConnection as bc
import os
from dollarpy import Point


import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

def get_Image_Paths():
    directories = os.listdir("data")
    return directories


def main():
    brain = classifier.Classifier()
    extractor = tracker.Tracker()


    dirs = get_Image_Paths()
    unrecognized = []
    for dir in dirs:
     points = extractor.GetLandmarksFromImage(
        os.path.join("data" + "\\" + dir))
     label = dir[0]

     if points is None:
        unrecognized.append(label)
        continue
    brain.pointsToTemplate(points=points, label=label)
    


def add_text_to_image(image,letter,conf):
    # Define the font and other properties of the text
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (255, 255, 255) # white
    line_type = 2

# Add the text to the image
    cv2.putText(image, "Letter : " + letter, (0, 50), font, font_scale, font_color, line_type)
    cv2.putText(image, "confidence : " + str(conf), (0, 100), font, font_scale, font_color, line_type)
    
    return image


import cv2
import mediapipe as mp

def track_hands():
    
    brain = classifier.Classifier()
    extractor = tracker.Tracker()
    dirs = get_Image_Paths()
    unrecognized = []
    for dir in dirs:
     points = extractor.GetLandmarksFromImage(
        os.path.join("data" + "\\" + dir))
     label = dir[0]

     if points is None:
        unrecognized.append(label)
        continue
     if points is not None:
        brain.pointsToTemplate(points=points, label=label)
         
         
    
    print (unrecognized)
    
    # Initialize Mediapipe hands class
    mp_hands = mp.solutions.hands

    # Initialize camera capture
    cap = cv2.VideoCapture(0)
   
    
    
    # Start capturing and processing frames
    with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:

        while cap.isOpened():

            # Read frame from camera
            success, image = cap.read()
            if not success:
                break

            # Convert image to RGB
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Process image with Mediapipe hands
            results = hands.process(image)

            # Draw hand landmarks on the image
            if results.multi_hand_landmarks:
                landmarks = []
                for lm in results.multi_hand_landmarks:
                    for idx,landmark in enumerate( lm.landmark):
                        landmarks.append(Point (landmark.x,landmark.y))
                        
                    #Prediction is here    
                pred =brain.recognizePoints(landmarks)
                image = add_text_to_image(image=image,letter=pred[0],conf=pred[1])

                    
                for hand_landmarks in results.multi_hand_landmarks:
                    mp.solutions.drawing_utils.draw_landmarks(
                        image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Show the image
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            
            cv2.imshow('Hand Tracking', image)

            # Exit on ESC
            if cv2.waitKey(5) & 0xFF == 27:
                break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

    
track_hands()