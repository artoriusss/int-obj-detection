import kaggle
import zipfile
import os
from pathlib import Path

DATASET_ID = 'rsna-pneumonia-detection-challenge'

cur_dir = Path(__file__).resolve()
target_dir = cur_dir.parents[2] / 'data' / 'raw'

print("Saving raw data to:" + str(target_dir))

zip_path = target_dir / f'{DATASET_ID}.zip'

kaggle.api.authenticate()
kaggle.api.competition_download_files(DATASET_ID, path=target_dir, force=True, quiet=False)

with zipfile.ZipFile(target_dir / f'{DATASET_ID}.zip', 'r') as zip_ref:
    zip_ref.extractall(target_dir)

os.remove(zip_path)