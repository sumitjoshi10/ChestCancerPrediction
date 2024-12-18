from ChestCancerPrediction.config.configuration import ConfigurationManager
from ChestCancerPrediction.components.model_evaluation import Evaluation
from ChestCancerPrediction import logger
from ChestCancerPrediction.exception import CustomeException
import sys

STAGE_NAME = "Model Evaluation"


class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(eval_config)
            evaluation.evaluation()
            evaluation.log_into_mlflow()
            
        except Exception as e:
            raise CustomeException(e, sys)
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx====================================x")
    except Exception as e:
        raise CustomeException(e, sys)
