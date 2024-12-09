import os
import sys
import zipfile
import gdown
from ChestCancerPrediction import logger
from ChestCancerPrediction.exception import CustomeException
from ChestCancerPrediction.utils.common import get_size
from ChestCancerPrediction.config.configuration import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self) -> str:
        '''
        Fetch data from the google drive
        '''
        try:
            dataset_url = self.config.source_URL
            zip_download_url = self.config.local_data_file
            os.makedirs(self.config.root_dir,exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_url}")
            
            file_id = dataset_url.split("/")[-2]
            download_link = f"https://drive.google.com/uc?id={file_id}&confirm=t"
            gdown.download(download_link,zip_download_url,quiet=False)
            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_url}")
            
        except Exception as e:
            raise CustomeException(e,sys)
        
    def extract_zip_file(self):
        '''
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        '''
        try:
            unzip_path = self.config.unzip_dir
            with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
                zip_ref.extractall(unzip_path)
        
        except Exception as e:
            raise CustomeException(e,sys)