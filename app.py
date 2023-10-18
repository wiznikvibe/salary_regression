import os, sys
from src.logger import logging
from src.exception import CustomException

if __name__ == '__main__':
    try:
        logging.info("Logging File Setup Complete.")
        logging.info("Exception Generated")
        a = 5 / 0
        logging.info(a)
        
    except Exception as e: 
        # logging.info(CustomException(e, sys))
        raise CustomException(e, sys)