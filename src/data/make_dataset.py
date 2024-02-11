from file_helpers import dcm_to_jpg, row_to_txt_file, get_patient_ids, data_to_yolo_format

import pandas as pd 
import os
from pathlib import Path

cur_dir = os.path.join(os.path.dirname(__file__))
cur_dir = Path(cur_dir).resolve()

data_dir = cur_dir.parents[1] / 'data'
raw_data_dir = data_dir / 'raw' / 'rsna-pneumonia-detection-challenge'

train_images_dir = raw_data_dir / 'stage_2_train_images'
labels_path = raw_data_dir / 'stage_2_train_labels.csv'

patient_ids = get_patient_ids(raw_data_dir/'stage_2_train_images')
labels_df = pd.read_csv(labels_path)

RAW_DCM_TRAIN = raw_data_dir / 'stage_2_train_images'
RAW_CSV_TRAIN = raw_data_dir / 'stage_2_train_labels.csv'

TXT_DIR_TRAIN = data_dir / 'processed' / 'labels' / 'train'
JPG_DIR_TRAIN = data_dir / 'processed' / 'images' / 'train'

#TXT_DIR_VAL = cur_dir.parents[1] / 'data' / 'processed' / 'labels' / 'val'
#JPG_DIR_VAL = cur_dir.parents[1] / 'data' / 'processed' / 'images' / 'val'

os.makedirs(TXT_DIR_TRAIN, exist_ok=True)
os.makedirs(JPG_DIR_TRAIN, exist_ok=True)

data_to_yolo_format(RAW_DCM_TRAIN, labels_df, JPG_DIR_TRAIN, TXT_DIR_TRAIN, patient_ids)
