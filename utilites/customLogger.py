import logging

class LogGen:
    @staticmethod    #Directly called without creating any object
    def loggen():
        logging.basicConfig(filename=".\\Logs\\test.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
