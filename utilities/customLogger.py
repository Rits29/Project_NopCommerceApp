import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        """
        Creates and returns a logger that writes to ./Logs/automation.log.
        Ensures the Logs folder exists.
        """

        # Make sure the Logs folder exists in your project root
        os.makedirs("./Logs", exist_ok=True)

        logger = logging.getLogger("automationLogger")

        # Avoid adding multiple handlers if loggen() is called multiple times
        if not logger.handlers:
            logger.setLevel(logging.INFO)

            # Create a file handler for logging
            file_handler = logging.FileHandler("./Logs/automation.log")
            formatter = logging.Formatter(
                fmt="%(asctime)s - %(levelname)s - %(message)s",
                datefmt="%m/%d/%Y %I:%M:%S %p"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger

        
        
        
        
        
        
        
        # Set up logging configuration
       # logging.basicConfig(filename = "./Logs/automation.log",
        #                format='%(asctime)s:%(levelname)s:%(message)s',
         #               datefmt='%m/%d/%Y %I:%M:%S %p')
        #logger = logging.getLogger()
        #logger.setLevel(logging.INFO)   
        #return logger