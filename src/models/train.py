from ultralytics import YOLO
from src.models.path import CONFIG_PATH

class Train():
    def train(self, epochs=100,imgsize=640,batchsize=-1):
        model = YOLO('yolov8n.pt')
        model.train(data=CONFIG_PATH, epochs=epochs, imgsz=imgsize, batch=batchsize)