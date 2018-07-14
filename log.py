import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
formatter=logging.Formatter('%(asctime)s %(name) -12s %(levelname) -8s %(message)s')

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this,too')
logging.error('And this , too')
