from ChestCancerPrediction.config.configuration import ConfigurationManager
from ChestCancerPrediction.components.prepare_base_model import PreapareBaseModel
from ChestCancerPrediction import logger
from ChestCancerPrediction.exception import CustomeException
import sys

STAGE_NAME = "Prepare Base Model Stage"


class PrepareBaseModelPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PreapareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
            
        except Exception as e:
            raise CustomeException(e,sys)
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx====================================x")
    except Exception as e:
        raise CustomeException(e, sys)


