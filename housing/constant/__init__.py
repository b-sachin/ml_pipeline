import os
from datetime import datetime

ROOT_DIR = os.getcwd()  # to get current working directory

CONFIG_DIR = "config"
CONFIG_FILE_NAME = 'config.yaml'
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

# Training pipeline related variable
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME = "pipeline_name"

# Data Ingestion related variable

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_INGESTED_DIR_KEY = "ingested_dir"
DATA_INGESTION_INGESTED_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_INGESTED_TEST_DIR_KEY = "ingested_test_dir"


# Data Validation related variable

DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIDATION_SCHEMA_DIR_KEY = "schema_dir"
DATA_VALIDATION_SCHEMA_FILE_NAME_KEY = "schema_file_name"
DATA_VALIDATION_ARTIFACT_DIR_NAME = "data_validation"
DATA_VALIDATION_REPORT_FILE_NAME = "report_file_name"
DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY = "report_page_file_name"

# Dataset Schema related variables

DATASET_SCHEMA_COLUMNS = "columns"
DATASET_SCHEMA_TARGET_COLUMN = "target_column"
DATASET_SCHEMA_DOMAIN_VALUE = "domain_value"
DATASET_SCHEMA_NUMERICAL_COLUMN = "numerical_columns"
DATASET_SCHEMA_CATEGORICAL_COLUMN = "categorical_columns"

# Data Transformation related variable

DATA_TRANSFORMATION_ARTIFACT_DIR = "data_transformation"
DATA_TRANSFORMATION_CONFIG_KEY = "data_transformation_config"
DATA_TRANSFORMATION_ADD_BEDROOM_PER_ROOM_KEY = "add_bedroom_per_room"
DATA_TRANSFORMATION_TRANSFORMED_DIR_KEY = "transformed_dir"
DATA_TRANSFORMATION_TRANSFORMED_TRAIN_DIR_KEY  = "transformed_train_dir"
DATA_TRANSFORMATION_TRANSFORMED_TEST_DIR_KEY = "transformed_test_dir"
DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY = "preprocessing_dir"
DATA_TRANSFORMATION__PREPROCESSED_OBJECT_FILE_NAME_KEY = "preprocessed_object_file_name"

COLUMN_TOTAL_ROOMS = "total_rooms"
COLUMN_POPULATION = "population"
COLUMN_HOUSEHOLDS = "households"
COLUMN_TOTAL_BEDROOM = "total_bedrooms"


# Model Trainer related Variable

MODEL_TRAINER_ARTIFACT_DIR = "model_trainer"
MODEL_TRAINER_CONFIG_KEY="model_trainer_config"
MODEL_TRAINER_TRAINED_MODEL_DIR_KEY="trained_model_dir"
MODEL_TRAINER_TRAINED_MODEL_FILE_NAME_KEY="model_file_name"
MODEL_TRAINER_BASE_ACCURACY_KEY="base_accuracy"
MODEL_TRAINER_MODEL_CONFIG_DIR_KEY="model_config_dir"
MODEL_TRAINER_MODEL_CONFIG_FILE_NAME_KEY="model_config_file_name"

# Model Evaluation related variable

MODEL_EVALUATION_CONFIG_KEY = "model_evaluation_config"
MODEL_EVALUATION_FILE_NAME_KEY = "model_evaluation_file_name"
MODEL_EVALUATION_ARTIFACT_DIR = "model_evaluation"

BEST_MODEL_KEY = "best_model"
MODEL_PATH_KEY = "model_path"
HISTORY_KEY = "history"

# Model Pusher config key
MODEL_PUSHER_CONFIG_KEY = "model_pusher_config"
MODEL_PUSHER_MODEL_EXPORT_DIR_KEY = "model_export_dir"

EXPERIMENT_DIR_NAME="experiment"
EXPERIMENT_FILE_NAME="experiment.csv"
