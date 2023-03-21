from dollarpy import Recognizer, Template, Point

class Classifier:
    def __init__(self):
        self.templates = []
        self.train_on_predfined_videos()
        self.recognizer = Recognizer(self.templates)
    def train_on_predfined_videos(self):
        pass
    def videoPathToTemplate(self,path):
        pass
    def imagePathToTemplate(self,path):
        pass
        
    def recognizePoints(self,points):
        return self.recognizer.recognize(points)
        
    def pointsToTemplate(self,label,points):
        # if len(points) == 0:
        #      raise Exception("list is empty")
        temp =Template(label, points)
        self.templates.append(temp)
        return temp
        

    