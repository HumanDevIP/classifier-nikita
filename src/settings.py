import os
from dotenv import load_dotenv

load_dotenv("../dev.env")


MLFLOW_TRACKING_URI: str = os.getenv('MLFLOW_TRACKING_URI')
MLFLOW_TRACKING_USERNAME: str = os.getenv('MLFLOW_TRACKING_USERNAME')
MLFLOW_TRACKING_PASSWORD: str = os.getenv('MLFLOW_TRACKING_PASSWORD')

