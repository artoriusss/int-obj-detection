from path import WEIGHTS_PATH, TEST_IMGS_DIR, REPORTS_DIR
from train import results
from predict_and_save import *

from ultralytics import YOLO
import os
import pandas as pd

best_model = YOLO(WEIGHTS_PATH)
predict_and_save(best_model)