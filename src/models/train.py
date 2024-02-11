from ultralytics import YOLO
from path import *
import os 

model = YOLO('yolov8n.pt')
results = model.train(data=CONFIG_PATH, epochs=1, imgsz=640, batch=-1)