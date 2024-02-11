import os
from pathlib import Path

cur_dir       =   os.path.join(os.path.dirname(__file__))
cur_dir       =   Path(cur_dir).resolve()

DATA_DIR      =   cur_dir.parents[1] / 'data'
RAW_DIR       =   DATA_DIR / 'raw'

labels_path   =   RAW_DIR / 'stage_2_train_labels.csv'

DCM_RAW       =   RAW_DIR / 'stage_2_train_images'

PROCESSED_DIR =   DATA_DIR / 'processed'

JPG_DIR       =   DATA_DIR / 'processed' / 'images' 
TXT_DIR       =   DATA_DIR / 'processed' / 'labels'

DCM_RAW_TEST  =   RAW_DIR / 'stage_2_test_images'
TEST_DIR      =   DATA_DIR / 'test' 