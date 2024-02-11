import pandas as pd
import os
from pathlib import Path
from file_helpers import get_patient_ids

cur_dir       =   os.path.join(os.path.dirname(__file__))
cur_dir       =   Path(cur_dir).resolve()

DATA_DIR      =   cur_dir.parents[1] / 'data'
RAW_DIR       =   DATA_DIR / 'raw' / 'rsna-pneumonia-detection-challenge'

labels_path   =   RAW_DIR / 'stage_2_train_labels.csv'

patient_ids   =   get_patient_ids(RAW_DIR/'stage_2_train_images')
labels_df     =   pd.read_csv(labels_path)

cur_dir       =   os.path.join(os.path.dirname(__file__))
cur_dir       =   Path(cur_dir).resolve()

DCM_RAW       =   RAW_DIR / 'stage_2_train_images'
CSV_RAW       =   RAW_DIR / 'stage_2_train_labels.csv'

JPG_DIR       =   DATA_DIR / 'processed' / 'images' 
TXT_DIR       =   DATA_DIR / 'processed' / 'labels'

PROCESSED_DIR =   DATA_DIR / 'processed'