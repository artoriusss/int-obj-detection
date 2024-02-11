import os
from getpass import getpass

class Authenticator:
    def authenticate(self):
        username = input('Enter your Kaggle username: ')
        key = getpass('Enter your Kaggle API key: ')

        os.environ['KAGGLE_USERNAME'] = username
        os.environ['KAGGLE_KEY'] = key
