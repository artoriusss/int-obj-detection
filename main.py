from src.main import make_dataset

def main():
    data = make_dataset.DataPrep()
    data.split_data()
    data.create_config()
    data.load_test_images()
    
if __name__ == '__main__':
    main()

