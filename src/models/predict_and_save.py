from path import TEST_IMGS_DIR, REPORTS_DIR

import os
import pandas as pd
from ultralytics import YOLO

def predict_and_save(model):
    results = model.predict(TEST_IMGS_DIR, verbose=False)

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

