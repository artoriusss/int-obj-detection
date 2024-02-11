from path import CST_WEIGHTS_PATH
from predict_and_save import *

from ultralytics import YOLO

pretrained_model = YOLO(CST_WEIGHTS_PATH)
predict_and_save(pretrained_model)