import logging
from logging.handlers import RotatingFileHandler
import os

# Retrieving the absolute path of the parent folder
log_directory = os.path.dirname(os.path.abspath(__file__))

# Logger configuration with rotation
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_file = os.path.join(log_directory, 'app.log')  # Full path to the log file

# Creation of the RotatingFileHandler instance
file_handler = RotatingFileHandler(log_file, mode='a', encoding='utf-8', maxBytes=1024 * 1024, backupCount=5)
file_handler.setFormatter(log_formatter)

# Log level configuration
file_handler.setLevel(logging.INFO)

# Main logger configuration
logger = logging.getLogger('app_logger')
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)

# Save info
def log_info(message):
    """
    Sauvegarde une information dans le fichier de log.
    """
    logger.info(message, exc_info=True)

# Save error
def log_error(message):
    """
    Sauvegarde une erreur dans le fichier de log.
    """
    logger.error(message, exc_info=True)