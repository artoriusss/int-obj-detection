from pathlib import Path  
import os

cur_dir       =   Path(__file__).resolve()
CONFIG_PATH   =   cur_dir.parents[2] / 'data' / 'processed' / 'config.yaml'