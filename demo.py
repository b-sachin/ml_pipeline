from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
import os,sys
from housing.config.configuration import Configuration

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()

    except Exception as e:
        logging.error(f"{e}")
        raise HousingException(e,sys) from e
        
if __name__ == "__main__":
    main()

