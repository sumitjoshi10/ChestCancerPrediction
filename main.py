from ChestCancerPrediction import logger
from ChestCancerPrediction.exception import CustomeException
import sys

from ChestCancerPrediction.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from ChestCancerPrediction.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx====================================x")
except Exception as e:
    raise CustomeException(e, sys)


STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx====================================x")
except Exception as e:
    raise CustomeException(e, sys)
