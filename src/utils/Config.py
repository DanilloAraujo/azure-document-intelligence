import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = os.getenv('DOCUMENT_INTELIGENCE_ENDPOINT')
    KEY = os.getenv('DOCUMENT_INTELIGENCE_KEY')
    AZURE_STORAGE_CONNECTION = os.getenv('ACCESS_KEY')
    CONTAINER_NAME = os.getenv('CONTAINER_NAME')