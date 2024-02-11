from src.data.data_prep import DataPrep
from src.data.kaggle_dataset import KaggleDataset 
from src.data.authenticator import Authenticator

from src.models.path import CST_WEIGHTS_PATH,TEST_IMGS_DIR
from src.models.train import Train
from src.models.inference import Inference

def main():
    authenticator = Authenticator()
    authenticator.authenticate()

    kaggle_dataset = KaggleDataset()
    kaggle_dataset.load()

    data_prep = DataPrep()
    data_prep.split_data()
    data_prep.create_config()
    data_prep.load_test_images()

    train_model = Train()
    # uncomment to train
    # train_model.train()

    inference = Inference(CST_WEIGHTS_PATH)
    inference.predict(TEST_IMGS_DIR)
    
if __name__ == '__main__':
    main()

