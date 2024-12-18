from ChestCancerPrediction import logger
from ChestCancerPrediction.exception import CustomeException
import sys

from ChestCancerPrediction.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from ChestCancerPrediction.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from ChestCancerPrediction.pipeline.stage_03_model_trainer import ModelTrainerPipeline
from ChestCancerPrediction.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx====================================x")
except Exception as e:
    raise CustomeException(e, sys)


STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    prepare_base_model = PrepareBaseModelPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx====================================x")
except Exception as e:
    raise CustomeException(e, sys)



STAGE_NAME = "Model Trainer"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx====================================x")
except Exception as e:
    raise CustomeException(e, sys)




STAGE_NAME = "Model Evaluation"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    eval = ModelEvaluationPipeline()
    eval.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx====================================x")
except Exception as e:
    raise CustomeException(e, sys)
