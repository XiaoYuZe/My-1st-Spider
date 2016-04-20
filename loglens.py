import logging
import datetime

logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename= datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')+'.log',
                filemode='w')
a = 'wakiea'
logging.debug('debug '+a+' model')
logging.info('info model')
logging.warning('warning model')
logging.error('error model')
logging.critical('critical model')