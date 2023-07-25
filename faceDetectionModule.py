# import packages and module required
import cv2
from FaceMeshModule import FaceMeshDetector


# blue print to check if face is present or not
class faceDetector():

    def __init__(self):
        self.detector=FaceMeshDetector(maxFaces=1)

    def findFace(self,img):
        self.img,self.faces=self.detector.findFaceMesh(img,draw=False)
        return img

    def isFacePresent(self):
        if self.faces:
            return True
        return False

    def distance(self):
        if self.isFacePresent():
            face=self.faces[0]
            pointLeft=face[145]
            pointRight=face[374]

            #just for visulization
            cv2.line(self.img,pointLeft,pointRight,(0,200,0),3)
            cv2.circle(self.img,pointLeft,5,(255,0,255),cv2.FILLED)
            cv2.circle(self.img, pointRight, 5, (255, 0, 255), cv2.FILLED)

            w,_=self.detector.findDistance(pointLeft,pointRight)
            W = 6.3
            #finding focal length

            # d=50
            # f=(w*d)/W
            # print(f)

            #finding distance

            f=840
            d=(W*f)/w
            # print(d)
            return d
        else:
            return float('inf')

def main():
    cap = cv2.VideoCapture(0)
    # detector = FaceMeshDetector(maxFaces=1)
    detector=faceDetector()
    while True:
        success,img=cap.read()
        detector.findFace(img)
        detector.distance()
        cv2.imshow("Image", detector.img)
        cv2.waitKey(1)

    pass


if __name__=="__main__":
    main()