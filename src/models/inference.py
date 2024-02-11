from src.models.path import REPORTS_DIR
import os
import pandas as pd

from ultralytics import YOLO

img_size = 1024

class Inference:
    def __init__(self, best_weights_path):
        self.model = YOLO(best_weights_path)

    def predict(self, test_images_dir):
        print('Predicting...')
        results = self.model.predict(test_images_dir, conf=0.08)
        print('Finished...')
        print('Creating submission...')

        submit_dict = {"patientId": [], "PredictionString": []}

        for result in results:
            patient_id = os.path.splitext(os.path.basename(result.path))[0]
            submit_dict["patientId"].append(patient_id)
            submit_line=''
            for b in result.boxes:
                xywhn = b.xywhn.tolist()
                rcx, rcy, rw, rh = xywhn[0][0],xywhn[0][1],xywhn[0][2],xywhn[0][3]
                conf = float(b.conf)
                x = (rcx-rw/2)*img_size
                y = (rcy-rh/2)*img_size
                w = rw*img_size
                h = rh*img_size
                submit_line += "{} {} {} {} {} ".format(conf, x, y, w, h)
            submit_dict["PredictionString"].append(submit_line)

        pd.DataFrame(submit_dict).to_csv(REPORTS_DIR, index=False)