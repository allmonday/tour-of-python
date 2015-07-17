import logging
import os
# logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'), level = logging.DEBUG)
logging.basicConfig(level = logging.DEBUG,
                    format="%(asctime)s %(levelname)s:%(message)s",
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.debug('this is a message')
