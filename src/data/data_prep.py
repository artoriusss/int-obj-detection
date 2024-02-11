import os
import yaml
import pandas as pd
import src.data.file_helper as file_helper
from src.data.path import *
from sklearn.model_selection import train_test_split

class DataPrep():
    def __init__(self):
        self.helper = file_helper.FileHelper()
        self._create_dirs()

    def create_config(self):
        config_obj = {
            'path': str(DATA_DIR / 'processed'),
            'train': 'images/train',
            'val': 'images/val',
            'names': {
                0: 'pneumonia'
            }
        }

        path_yaml = str(os.path.join(PROCESSED_DIR,'config.yaml'))

        with open(path_yaml, 'w') as file:
            yaml.dump(config_obj, file, default_flow_style=False, 
                        sort_keys=False, indent=4, allow_unicode=False)

    def split_data(self):
        patient_ids = self.helper.get_patient_ids(RAW_DIR/'stage_2_train_images')
        train_ids, _ = train_test_split(patient_ids, test_size=0.2, random_state=42)
        labels_df = pd.read_csv(labels_path)
        self.helper.data_to_yolo_format(DCM_RAW, labels_df, JPG_DIR, TXT_DIR, train_ids)
        
    def load_test_images(self):
        self.helper.load_test_images(DCM_RAW_TEST, TEST_DIR)
    
    def _create_dirs(self):
        os.makedirs(TXT_DIR / 'val', exist_ok=True)
        os.makedirs(JPG_DIR / 'val', exist_ok=True)
        os.makedirs(TXT_DIR / 'train', exist_ok=True)
        os.makedirs(JPG_DIR / 'train', exist_ok=True)
        os.makedirs(TEST_DIR, exist_ok=True)