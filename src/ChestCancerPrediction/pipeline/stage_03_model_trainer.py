from ChestCancerPrediction.config.configuration import ConfigurationManager
from ChestCancerPrediction.components.model_trainer import Training
from ChestCancerPrediction import logger
from ChestCancerPrediction.exception import CustomeException
import sys

STAGE_NAME = "Model Trainer"


class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()
            
        except Exception as e:
            raise e
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx====================================x")
    except Exception as e:
        raise CustomeException(e, sys)
