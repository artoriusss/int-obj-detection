from file_helpers import *
from path import *

import pandas as pd 
import os
import yaml
from sklearn.model_selection import train_test_split
from pathlib import Path

os.makedirs(TXT_DIR / 'val', exist_ok=True)
os.makedirs(JPG_DIR / 'val', exist_ok=True)
os.makedirs(TXT_DIR / 'train', exist_ok=True)
os.makedirs(JPG_DIR / 'train', exist_ok=True)

train_ids, val_ids = train_test_split(patient_ids, test_size=0.2, random_state=42)

data_to_yolo_format(DCM_RAW, labels_df, JPG_DIR, TXT_DIR, train_ids)

config_obj = {
    'path': str(DATA_DIR / 'processed'),
    'train': str(JPG_DIR / 'train'),
    'val': str(JPG_DIR / 'val'),
    
    'names': ['pneumonia']
}

path_yaml = str(os.path.join(PROCESSED_DIR,'config.yaml'))

with open(path_yaml, 'w') as file:
    yaml.dump(config_obj, file, default_flow_style=False, 
                sort_keys=False, indent=4, allow_unicode=False)

load_test_images(DCM_RAW_TEST, TEST_DIR)