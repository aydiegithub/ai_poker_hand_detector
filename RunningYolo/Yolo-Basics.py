from ultralytics import YOLO
import cv2


model = YOLO('Yolo-Weights/yolov8m.pt')
result = model("images/img2.jpg", show = True)
cv2.waitKey(0)