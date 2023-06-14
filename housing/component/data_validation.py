from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from housing.constant import DATASET_SCHEMA_COLUMNS, DATASET_SCHEMA_DOMAIN_VALUE
from housing.util.util import read_yaml_file
import os, sys
import pandas as pd
# from evidently.model_profile import Profile
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
from evidently.metric_preset import TargetDriftPreset

from evidently.test_suite.test_suite import TestSuite
from evidently.test_preset import NoTargetPerformanceTestPreset
#from evidently.model_profile.sections import DataDriftProfileSection
#from evidently.dashboard import Dashboard
#from evidently.dashboard.tabs import DataDriftTab


import json

class DataValidation:

    def __init__(self, 
                 data_validation_config:DataValidationConfig,
                 data_ingestion_artifact:DataIngestionArtifact) -> None:
        try:
            logging.info(f"{'='*20}Data Validation log started.{'='*20}")
            self.data_validation_config=data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e

    def get_train_and_test_df(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df,test_df
        except Exception as e:
            raise HousingException(e,sys) from e

    def is_train_test_file_exists(self) -> bool:
        try:
            logging.info("Checking if training and testing file exists?")
            is_train_file_exist = False
            is_test_file_exist = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)

            is_available = is_train_file_exist and is_test_file_exist

            if not is_available:
                training_file = self.data_ingestion_artifact.train_file_path
                testing_file = self.data_ingestion_artifact.test_file_path
                raise Exception(f"Training file: {training_file} or Testing file: {testing_file} is not present")

            logging.info(f"is train and test file exists -> {is_available}")
            return is_available

        except Exception as e:
            raise HousingException(e,sys) from e

    def validate_dataset_schema(self) -> bool:
        try:
            validation_status = False

            logging.info("validating dataset schema")
            
            schema_file_path = self.data_validation_config.schema_file_path
            schema_info = read_yaml_file(file_path = schema_file_path )

            # 1. Cheking column count
            logging.info("Checking if column count in training and testing set matches to column count specified in schema")
            is_column_count_match = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            train_data_frame,test_data_frame = self.get_train_and_test_df()

            train_column_count = len(train_data_frame.columns)
            test_column_count = len(test_data_frame.columns)

            schema_column_count = len(schema_info[DATASET_SCHEMA_COLUMNS])

            if (train_column_count == schema_column_count) and (test_column_count == schema_column_count):
                is_column_count_match = True
                logging.info(f"is column count of schema matches with taining and testing set column count -> {is_column_count_match}")
            else:
                raise Exception(f"""Training Dataset Column count: {train_column_count} 
                                    or Testing Dataset Column count:{test_column_count} 
                                    does not match to Schema Column count: {schema_column_count}""")

            # 2. Checking Values of Categorical columns
            logging.info(f"checking the values of 'ocean proximity' column of Schema Dataset with Training and Testing Dataset")
            
            domain_values_match = False
            domain_value_columns = schema_info[DATASET_SCHEMA_DOMAIN_VALUE]
            
            schema_column_domain_values = list(domain_value_columns.values())[0]
            
            train_cat = train_data_frame.loc[:,list(train_data_frame.dtypes == 'object')]
            train_cat_df = pd.DataFrame(train_cat.value_counts())
            train_cat_df.reset_index(inplace=True)
            train_column_domain_values = list(train_cat_df.iloc[:,0])


            test_cat = test_data_frame.loc[:,list(test_data_frame.dtypes == 'object')]
            test_cat_df = pd.DataFrame(test_cat.value_counts())
            test_cat_df.reset_index(inplace=True)
            test_column_domain_values = list(test_cat_df.iloc[:,0])

            if (train_column_domain_values.sort() == schema_column_domain_values.sort()) and \
                (test_column_domain_values.sort() == schema_column_domain_values.sort()):
                domain_values_match = True
                logging.info(f"domain values of schema column matches with taining and testing set domain value column -> \
                            {domain_values_match}")
            else:
                raise Exception(f"""Domain values of Training Dataset: {train_column_domain_values.sort()} 
                                  or Domain values of Testing Dataset: {test_column_domain_values.sort()} 
                                  does not match with Domain values of Schema Column: {schema_column_domain_values.sort()}""")

            # 3. Checking all column names

            logging.info(f"checking all column names of Schema Dataset with Training and Testing Dataset")
            
            all_column_names_match = False
            
            schema_columns = schema_info[DATASET_SCHEMA_COLUMNS]
            schema_columns_list = list(schema_columns.keys())

            train_column_list = list(train_data_frame.columns)
            test_column_list = list(test_data_frame.columns)

            if (train_column_list.sort() == schema_columns_list.sort()) and (test_column_list.sort() == schema_columns_list.sort()):
                all_column_names_match = True
                logging.info(f"all column names of schema matches with taining and testing set column names -> {all_column_names_match}")
            else:
                raise Exception(f"""Training Dataset Column names: {train_column_list.sort()} 
                                  or Testing Dataset Column names: {test_column_list.sort()} 
                                  does not match with Schema Column names: {schema_columns_list.sort()}""")

            validation_status = all([is_column_count_match, domain_values_match, all_column_names_match])
            
            logging.info(f"is dataset schema validation successful -> {validation_status}")
            return validation_status
        except Exception as e:
            raise HousingException(e,sys) from e

    def get_and_save_data_drift_report(self):
        try:
            # profile = Profile(sections=[DataDriftProfileSection()])
            drift_report = Report(metrics=[DataDriftPreset(), TargetDriftPreset()])
            
            train_data_frame,test_data_frame = self.get_train_and_test_df()
            
            # profile.calculate(train_data_frame,test_data_frame)
            drift_report.run(reference_data= train_data_frame, current_data=test_data_frame)

            # report = json.loads(profile.json())
            report = json.loads(drift_report.json())

            report_file_path = self.data_validation_config.report_file_path

            report_dir = os.path.dirname(report_file_path)
            os.makedirs(report_dir, exist_ok=True)

            with open(report_file_path,"w") as report_file:
                json.dump(report, report_file, indent = 6)
            return report
        except Exception as e:
            raise HousingException(e,sys) from e

    def save_data_drift_report_page(self):
        try:
            #dashboard = Dashboard(tabs = [DataDriftTab()])
            no_target_performance = TestSuite(tests=[NoTargetPerformanceTestPreset(),])
            
            train_data_frame,test_data_frame = self.get_train_and_test_df()
            
            #dashboard.calculate(train_data_frame,test_data_frame)
            no_target_performance.run(reference_data=train_data_frame,current_data=test_data_frame)
            
            report = json.loads(no_target_performance.json())

            report_page_file_path = self.data_validation_config.report_page_file_path

            report_page_dir = os.path.dirname(report_page_file_path)
            os.makedirs(report_page_dir, exist_ok=True)

            # dashboard.save(report_page_file_path)
            with open(report_page_file_path,"w") as report_file:
                json.dump(report, report_file, indent = 6)

        except Exception as e:
            raise HousingException(e,sys) from e
    
    def is_data_drift(self) -> bool:
        try:
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()
            return True
        except Exception as e:
            raise HousingException(e,sys) from e

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()
            self.is_data_drift()

            data_validation_artifact = DataValidationArtifact(schema_file_path=self.data_validation_config.schema_file_path,
                                                              report_file_path=self.data_validation_config.report_file_path,
                                                              report_page_file_path=self.data_validation_config.report_page_file_path,
                                                              is_validated=True,
                                                              message="Data Validation performed successfully.")
            
            logging.info(f"Data validation artifact: {data_validation_artifact}")

            return data_validation_artifact
        except Exception as e:
            raise HousingException(e,sys) from e

    def __del__(self):
        logging.info(f"{'='*20}Data Validation log Completed. {'='*20} \n\n")