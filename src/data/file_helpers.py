import pydicom
import cv2
import os
from tqdm import tqdm
import pandas as pd
import numpy as np


def get_patient_ids(folder_path):
    """
    Get the patient IDs from the filenames in the specified directory.
    Args:
        folder_path (str): The directory containing the patient images.
    Returns:
        patient_ids (list): A list of patient IDs.
    """
    patient_ids = []

    for filename in os.listdir(folder_path):
        patient_id = os.path.splitext(filename)[0]
        patient_ids.append(patient_id)

    return patient_ids

def dcm_to_jpg(dcm_dir: str, jpg_dir: str, patient_id):
    """
    Convert a DICOM image to a JPEG image and save it to the specified directory.
    Args:
        dcm_dir (str): The directory containing the DICOM images.
        img_dir (str): The directory to save the JPEG images.
        patient_id (str): The patient ID (used as an image filename).
    """
    jpg_img_path = os.path.join(jpg_dir, f'{patient_id}.jpg')

    if os.path.exists(jpg_img_path):
        return

    dcm_img_path = os.path.join(dcm_dir, f'{patient_id}.dcm')

    if not os.path.exists(dcm_img_path):
        return

    img_greyscale = pydicom.read_file(dcm_img_path).pixel_array
    img_rgb = np.stack([img_greyscale]*3, -1)
    cv2.imwrite(jpg_img_path, img_rgb) 


def row_to_txt_file(label_dir: str, patient_id, data=None):
    """
    Convert a row of a dataframe label to a txt file.
    Args:
        label_dir (str): The directory to save the label txt files.
        patient_id (str): The patient ID (used as a txt filename).
        data (pd.Series): The row of the label dataframe.
    """
    img_size = 1024

    if pd.isnull(data).any():
        return

    print('\n',data[0],data[1],'\n') 
    x_rel = data[0]/img_size
    y_rel = data[1]/img_size
    width_rel = data[2]/img_size
    height_rel = data[3]/img_size
    
    center_x_rel = x_rel + width_rel/2
    center_y_rel = y_rel + height_rel/2
    
    label_path = os.path.join(label_dir,f'{patient_id}.txt')
    
    with open(label_path, 'w') as file:
        line = f'0 {center_x_rel} {center_y_rel} {width_rel} {height_rel}\n'
        file.write(line)


def data_to_yolo_format(input_img_dir, train_labels_df, img_dir, label_dir, train_ids):
    """
    Convert the DICOM images and label dataframe to the YOLO format.
    Args:
        input_img_dir (str): The directory containing the DICOM images.
        train_labels_df (pd.DataFrame): The label dataframe.
        img_dir (str): The directory to save the JPEG images.
        label_dir (str): The directory to save the label txt files.
        train_ids (list): A list of patient IDs for the training set.
    """

    for row in tqdm(train_labels_df.values):
        patient_id = row[0]
        data = row[1:]
        
        final_dir_name = 'train' if patient_id in train_ids else 'val'
        
        img_final_dir =  os.path.join(img_dir,  final_dir_name)
        label_final_dir = os.path.join(label_dir,  final_dir_name)
        
        dcm_to_jpg(input_img_dir, img_final_dir, patient_id)
        row_to_txt_file(label_final_dir, patient_id,data)

def load_test_images(input_img_dir, img_dir):
    """
    Load test DICOM images to JPEG format, and save converted JPEG images to img_dir.
    Args:
        input_img_dir (str): The directory containing the DICOM images.
        img_dir (str): The directory to save the JPEG images.
    """
    for filename in os.listdir(input_img_dir):
        patient_id = os.path.splitext(filename)[0]
        dcm_to_jpg(input_img_dir, img_dir, patient_id)
