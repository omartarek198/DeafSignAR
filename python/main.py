import tracker
import classifier
import os

def get_Image_Paths():
    directories =  os.listdir("python\data")
    return directories


brain = classifier.Classifier()
extractor = tracker.Tracker()


dirs = get_Image_Paths()
unrecognized = []
for dir in dirs:
    points = extractor.GetLandmarksFromImage(os.path.join("python\\data" +"\\" + dir))
    label = dir[0]
     
    if points is None:
        unrecognized.append(label)
        continue
    brain.pointsToTemplate(points=points,label =label)



points = extractor.GetLandmarksFromImage("python\T_test.jpg")
print (points)
result =brain.recognizePoints(points=points)
print (result)
print (unrecognized)