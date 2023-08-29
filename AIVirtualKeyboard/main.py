import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

cap = cv.VideoCapture(0)
cap.set(3,1080)
cap.set(4,720)


detector = HandDetector(detectionCon=0.8,maxHands=2)
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L",';'],
        ["Z", "X", "C", "V", "B", "N", "M",',','.','/']]


def drawAll(img,buttonList):
    for button in buttonList: #1
        x, y = button.pos
        w, h = button.size
        cv.rectangle(img, button.pos, (x + w, y + h), (0, 0, 0), cv.FILLED)
        cv.putText(img, button.text, (x + 15, y + 80), cv.FONT_HERSHEY_SIMPLEX,
                   2, (255, 255, 200), 3)
    return img
class Button():
    def __init__(self,pos,text,size= [100, 100]):

        self.pos = pos
        self.text = text
        self.size = size
    #def draw(self,img):




buttonList = []

for i in range(len(keys)):

    for j, key in enumerate(keys[i]):
        buttonList.append(Button([120 * j + 50, 110 * i + 70], key))

while True:
    success,img = cap.read()
    hands,img = detector.findHands(img)

    img = drawAll(img,buttonList)
    # img = myButton.draw(img)
    # img = myButton2.draw(img)
    # img = myButton3.draw(img)

    #Hand - dict(lmList - bbox - center - type)





    if hands:
        #Hand1
        hand1 = hands[0]
        lmList1 = hand1["lmList"] ## 21 landmarks of hand
        bbox1 = hand1['bbox'] ## Bounding Box info x,y,w,h
        centerPoint1 = hand1['center']
        handType1 = hand1['type']
        # print(len(lmList1),lmList1)
        # print(bbox1)
        # print(centerPoint1)
        # print(handType1)


        # fingers1 = detector.fingersUp(hand1)
        # point1 = lmList1[8]
        # point2 = lmList1[12]
        #
        # length, info, img = detector.findDistance(point2, point1, img)
        if len(hands) ==2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  ## 21 landmarks of hand
            bbox2 = hand2['bbox']  ## Bounding Box info x,y,w,h
            centerPoint2 = hand2['center']
            handType2 = hand2['type']
            # fingers2 = detector.fingersUp(hand2)
            # print(len(lmList1), lmList1)
            # print(bbox1)
            # print(centerPoint1)
            # print(handType1)
            #
            # print(len(lmList2), lmList2)
            # print(bbox2)
            # print(centerPoint2)
            # print(handType2)
            # print(fingers1,fingers2)
            #print(handType1,handType2)

    #
    # if lmList1 or lmList2:
    #     for button in buttonList:
    #         x,y = button.pos
    #         w,h = button.size
    #
    #         if x< ((lmList1[8][0]) or (lmList2[8][0]))<x+w:
    #











    cv.imshow('Image',img)
    cv.waitKey(1)