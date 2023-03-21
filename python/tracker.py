
import mediapipe as mp  # Import mediapipe
import cv2  # Import opencv
# import csv
import os
import numpy as np
import matplotlib.pyplot as plt
from dollarpy import Point


class Tracker:
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils  # Drawing helpers
        self.mp_holistic = mp.solutions.holistic  # Mediapipe Solutions

        self.mp_drawing_styles = mp.solutions.drawing_styles

    def GetLandmarksFromVideo(self, path, show=True):
        cap = cv2.VideoCapture(path)  # web cam =0 , else enter filename
        points = []

        with self.mp_holistic.Holistic(min_detection_confidence=0.5) as holistic:
            print("inside")

            while cap.isOpened():
                ret, frame = cap.read()
                if ret == False:
                    break
                if ret == True:

                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    image.flags.writeable = False
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                    results = holistic.process(image)
                    if results.right_hand_landmarks is not None:

                        self.mp_drawing.draw_landmarks(image, results.right_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS,
                                                       self.mp_drawing.DrawingSpec(
                                                           color=(80, 22, 10), thickness=2, circle_radius=4),
                                                       self.mp_drawing.DrawingSpec(
                                                           color=(80, 44, 121), thickness=2, circle_radius=2)
                                                       )

                    # self.mp_drawing.draw_landmarks(image, results.left_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS,
                    #                      self.mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4),
                    #                      self.mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                    #                      )

                        hand_skelton = results.right_hand_landmarks.landmark
                        for landmark in hand_skelton:
                            points.append([landmark.x, landmark.y])
                        print(points[-1])

                    if show:
                        cv2.imshow("label", image)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
        print("done")
        return points

    def GetLandmarksFromImage(self, path):
        mp_hands = mp.solutions.hands
        landmarks = []

    # For static images:
        with mp_hands.Hands(
            static_image_mode=True,
            max_num_hands=1,

                min_detection_confidence=0.5) as hands:
            image = cv2.flip(cv2.imread(path), 1)
            results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            if results.multi_hand_landmarks is not None:
                
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS, self.mp_drawing_styles.get_default_hand_landmarks_style(
                    ), self.mp_drawing_styles.get_default_hand_connections_style())
                for lm in results.multi_hand_landmarks:
                    for idx,landmark in enumerate( lm.landmark):
                        landmarks.append(Point (landmark.x,landmark.y))
                        

                cv2.imshow("label", image)
                cv2.waitKey(10)
                return landmarks
    def GetLandmarksFromLiveImage(self, image):
        mp_hands = mp.solutions.hands
        landmarks = []

    # For static images:
        with mp_hands.Hands(
            static_image_mode=True,
            max_num_hands=1,

                min_detection_confidence=0.5) as hands:
            image = cv2.flip(image, 1)
            results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            if results.multi_hand_landmarks is not None:
                
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS, self.mp_drawing_styles.get_default_hand_landmarks_style(
                    ), self.mp_drawing_styles.get_default_hand_connections_style())
                for lm in results.multi_hand_landmarks:
                    for idx,landmark in enumerate( lm.landmark):
                        landmarks.append(Point (landmark.x,landmark.y))
                        

                cv2.imshow("label", image)
                cv2.waitKey(10)
                return landmarks

    # def method2(self, arg3):
    #     pass


def main():
    tracker = Tracker()
    print("start")
    # print(tracker.GetLandmarksFromVideo("C:\\Users\\Dell\Desktop\\deafSignAR\\python\\palm2.jpg",show=True))
    print(tracker.GetLandmarksFromImage(
        "data\\B_test.jpg"))
    print("done")


# main()
