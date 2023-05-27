from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
import os,sys
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        # data_validation_config = Configuration().get_data_transformation_config()
        # print(data_validation_config)

        # file_path = r"D:\Projects\ML Projects\ML_Project_01\ml_project1\housing\artifact\data_ingestion\2022-12-21-09-56-22\ingested_data\train\housing.csv"
        # schema_file_path = r"D:\Projects\ML Projects\ML_Project_01\ml_project1\config\schema.yaml"

        # df = DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)

        # print(df.info())

    except Exception as e:
        logging.error(f"{e}")
        raise HousingException(e,sys) from e
        

if __name__ == "__main__":
    main()

