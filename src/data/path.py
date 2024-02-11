import pandas as pd
import os
from pathlib import Path

cur_dir       =   os.path.join(os.path.dirname(__file__))
cur_dir       =   Path(cur_dir).resolve()

DATA_DIR      =   cur_dir.parents[1] / 'data'
RAW_DIR       =   DATA_DIR / 'raw' / 'rsna-pneumonia-detection-challenge'

labels_path   =   RAW_DIR / 'stage_2_train_labels.csv'

labels_df     =   pd.read_csv(labels_path)

cur_dir       =   os.path.join(os.path.dirname(__file__))
cur_dir       =   Path(cur_dir).resolve()

DCM_RAW       =   RAW_DIR / 'stage_2_train_images'
CSV_RAW       =   RAW_DIR / 'stage_2_train_labels.csv'

JPG_DIR       =   DATA_DIR / 'processed' / 'images' 
TXT_DIR       =   DATA_DIR / 'processed' / 'labels'

PROCESSED_DIR =   DATA_DIR / 'processed'

DCM_RAW_TEST  =   RAW_DIR / 'stage_2_test_images'
TEST_DIR      =   DATA_DIR / 'test' 