import tracker
import classifier
import client
import bluetoothConnection as bc
import os

import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

def get_Image_Paths():
    directories = os.listdir("python\data")
    return directories


def main():
    brain = classifier.Classifier()
    extractor = tracker.Tracker()


    dirs = get_Image_Paths()
    unrecognized = []
    for dir in dirs:
     points = extractor.GetLandmarksFromImage(
        os.path.join("python\\data" + "\\" + dir))
     label = dir[0]

     if points is None:
        unrecognized.append(label)
        continue
    brain.pointsToTemplate(points=points, label=label)
    




import cv2
import mediapipe as mp

def track_hands():
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