import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifact', "train.csv")
    test_data_path: str = os.path.join('artifact', "test.csv")
    raw_data_path: str = os.path.join('artifact', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv("/mnt/c/Users/HP/ml_projects/maintenance/notebook/data/predictive_maintenance.csv")
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Raw data saved successfully")

            # Prepairing X and Y
            X = df.drop(columns=['UDI','Product ID', 'Target', 'Failure Type'], axis=1)
            y = df['Failure Type']
            logging.info("Prepared feature dataframe X and label series y")

            # Combine X and y into a single DataFrame for splitting
            data = X.copy()
            data['Failure Type'] = y

            logging.info("Train/Test Split Initiated")
            train_set,test_set=train_test_split(data, test_size=0.2,random_state=42)

            # Replace special characters in column names 
            train_set.columns = train_set.columns.str.replace(r'[^\w\s]', '', regex=True)
            test_set.columns = test_set.columns.str.replace(r'[^\w\s]', '', regex=True)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.
            test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()


