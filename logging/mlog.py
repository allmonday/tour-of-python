import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('this message should go to the log file')
logging.warning('so should this')
logging.info('and this too')
