#read the data from various sources
import os
import sys
from source.logger import logging
from source.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)

@dataclass
class DataIngenstionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_csv: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.txt')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngenstionConfig()

    def initiate_data_ingestion(self):
        #to read the data...
        logging.info("entered data ingestion")
        try:
            df=pd.read_csv('C:\\ML\\notebook\\stud.csv')
            logging.info("read dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("train tst split is created")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("ingestion of data done")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_csv,
            )


        except Exception as e:
            raise CustomException

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()

