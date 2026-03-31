import os
import subprocess
from cnnClassifier import logger
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        # Check if the folder exists AND is not empty
        if os.path.exists(self.config.unzip_dir) and os.listdir(self.config.unzip_dir):
            logger.info("Data already exists in the artifacts folder. Skipping DVC pull to avoid redundancy.")

        else:
                try:
                    logger.info("Data directory is empty. Synchronizing with Azure via DVC...")
                    # We only run this if the folder is actually empty
                    subprocess.run(["dvc", "pull"], check=True)
                    logger.info("DVC Pull successful.")
                except Exception as e:
                    logger.error("DVC pull failed. If you are running 'dvc repro', ensure data was added manually first.")
                    # We don't raise the error here so the pipeline can attempt to continue 
                    # if the folder actually has data in it.

    def extract_zip_file(self):
        # We no longer need this because DVC pulls the unzipped folder!
        logger.info("Data is already managed by DVC in unzipped format. Skipping extraction.")
        pass