from ultralytics import YOLO
import cv2
import cvzone
import math
import PokerHandFunction
import MongoDBTest
from datetime import datetime

cap = cv2.VideoCapture(0) #For webcam
cap.set(propId=3,value=1280)
cap.set(propId=4,value=720)


model = YOLO("../Yolo-Weights/playingCards.pt")

classNames = ['10C', '10D', '10H', '10S',
              '2C', '2D', '2H', '2S',
              '3C', '3D', '3H', '3S',
              '4C', '4D', '4H', '4S',
              '5C', '5D', '5H', '5S',
              '6C', '6D', '6H', '6S',
              '7C', '7D', '7H', '7S',
              '8C', '8D', '8H', '8S',
              '9C', '9D', '9H', '9S',
              'AC', 'AD', 'AH', 'AS',
              'JC', 'JD', 'JH', 'JS',
              'KC', 'KD', 'KH', 'KS',
              'QC', 'QD', 'QH', 'QS']



while True:
    success, img = cap.read()
    resluts = model(img, stream=True)
    hand = []

    pokerHandRanks = {10: "Royal Flush", 9: "Straight Flush", 8: "Four of a Kind", 7: "Full House", 6: "Flush",
                      5: "Straight", 4: "Three of a Kind", 3: "Two Pair", 2: "Pair", 1: "High"}

    reversedPokerHandRanks = {value: key for key, value in pokerHandRanks.items()}


    # These staments used for branding and text
    cvzone.putTextRect(img, f'Poker Eye', (25, 60), scale=1.3, thickness=2,
                       colorT=(31, 18, 71), colorR=(201, 233, 107), font=cv2.FONT_HERSHEY_PLAIN)
    cvzone.putTextRect(img, f'Product of Aydie\'s Avenue', (22, 95), scale=0.8, thickness=1,
                       colorT=(31, 18, 71), colorR=(201, 233, 107), font=cv2.FONT_HERSHEY_PLAIN, offset=7)
    cvzone.putTextRect(img, f'visit: aydie.in/projects', (600, 700), scale=0.8, thickness=1,
                       colorT=(31, 18, 71), colorR=(201, 233, 107), font=cv2.FONT_HERSHEY_PLAIN, offset=6)

    for r in resluts:
        boxes = r.boxes
        for box in boxes:

            #-----Bounding Box-----
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            #print(x1, y1, x2, y2)
            #cv2.rectangle(img, pt1=(x1,y1), pt2=(x2,y2), color=(255,0,255), thickness=3 )

            w, h = x2-x1,y2-y1
            #bbox = int(x1), int(y1), int(w), int(h)
            cvzone.cornerRect(img, bbox = (x1,y1,w,h))

            #-----Cinfidence Level-----
            conf = math.ceil((box.conf[0]*100))/100

            #----Class Name-----
            cls = int(box.cls[0])

            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1.2, thickness=2,
                               colorT=(31,18,71), colorR=(201, 233, 117), font=cv2.FONT_HERSHEY_PLAIN)

            if conf > 0.8 :
                hand.append(classNames[cls])


    print(hand)
    hand = list(set(hand))
    print("Card Detected => ",hand)

    if len(hand) == 5:
        resluts = PokerHandFunction.findPokerHand(hand)
        print("Combination Detected => ",resluts)

        # upadte to the database
        time_ = datetime.now().strftime('%H:%M')
        dbresult_ = MongoDBTest.mongoDataBaseUpdater(str(resluts), str(hand), reversedPokerHandRanks[str(resluts)], time_)
        print("MongoDB Feedback => ",dbresult_,"\n\n")

        cvzone.putTextRect(img, f'Your Hand is {resluts}, Rank score is {reversedPokerHandRanks[str(resluts)]}', (475, 60), scale=1.5, thickness=2,
                           colorT=(31,18,71), colorR=(201, 233, 107), font=cv2.FONT_HERSHEY_PLAIN)

        cvzone.putTextRect(img, f'Combination -> {str(hand)}', (475, 100), scale=1, thickness=2,
                           colorT=(31, 18, 71), colorR=(201, 233, 107), font=cv2.FONT_HERSHEY_PLAIN)



    cv2.imshow("Image",img)
    cv2.waitKey(1)
