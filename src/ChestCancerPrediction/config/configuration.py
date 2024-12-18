import os
from ChestCancerPrediction.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from ChestCancerPrediction.utils.common import read_yaml, create_directories
from ChestCancerPrediction.entity.config_entity import (DataIngestionConfig,
                                                        PrepareBaseModelConfig,
                                                        TrainingConfig)
from pathlib import Path

class ConfigurationManager:
    def __init__(
        self,
        config_file_path = CONFIG_FILE_PATH,
        params_file_path = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=Path(config.unzip_dir),
            data_file_name = config.data_file_name
        )
        
        return data_ingestion_config
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])
        
        prepare_base_model = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            update_base_model_path= Path(config.update_base_model_path),
            params_image_size= self.params.IMAGE_SIZE,
            params_learning_rate= self.params.LEARNING_RATE,
            params_include_top= self.params.INCLUDE_TOP,
            params_weight= self.params.WEIGHTS,
            params_classes= self.params.CLASSES
        )
        
        return prepare_base_model

    def get_training_config(self) -> TrainingConfig:
        data_file_name = self.config.data_ingestion.data_file_name
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, data_file_name)
        # training_data = os.path.join(self.config.data_ingestion.unzip_dir, "Chest_CT_Scan_image_data")
        create_directories([
            training.root_dir
        ])
        
        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            update_base_model_path=Path(prepare_base_model.update_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config