from pathlib import Path  

cur_dir          =   Path(__file__).resolve()
CONFIG_PATH      =   cur_dir.parents[2] / 'data' / 'processed' / 'config.yaml'
WEIGHTS_PATH     =   cur_dir.parents[3] / 'runs' / 'detect' / 'train' / 'weights' / 'best.pt'
TEST_IMGS_DIR    =   cur_dir.parents[2] / 'data' / 'test'
REPORTS_DIR      =   cur_dir.parents[2] / 'reports' / 'submission.csv'

CST_WEIGHTS_PATH =   cur_dir.parents[0] / 'weights' / 'best.pt'