from ChestCancerPrediction import logger
from ChestCancerPrediction.exception import CustomeException
import sys

from ChestCancerPrediction.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx====================================x")
except Exception as e:
    raise CustomeException(e, sys)