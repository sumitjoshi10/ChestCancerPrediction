from ChestCancerPrediction.config.configuration import ConfigurationManager
from ChestCancerPrediction.components.data_ingestion import DataIngestion
from ChestCancerPrediction import logger
from ChestCancerPrediction.exception import CustomeException

import sys

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            
        except Exception as e:
            raise CustomeException(e,sys)
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx====================================x")
    except Exception as e:
        raise CustomeException(e, sys)