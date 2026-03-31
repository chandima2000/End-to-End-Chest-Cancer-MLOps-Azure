import sys
import os

# Ensure the src directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cnnClassifier import logger
from cnnClassifier.pipeline.data_ingestion import DataIngestionTrainingPipeline


logger.info("Starting the CNN Classifier ...")

if __name__ == "__main__":
    try:
        logger.info("Starting the data ingestion stage...")
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_pipeline.main()
        logger.info("Data ingestion stage completed successfully.")
    except Exception as e:
        logger.exception(e)




