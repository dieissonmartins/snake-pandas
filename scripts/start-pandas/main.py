import logging
import sys
import pandas

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

logging.info('-----------------------------')
logging.info('processing script test pandas')
logging.info('-----------------------------\n')

my_stores = {
    'stores': ['Supermercado BH', 'Supermercado NC'],
    'counters': [78, 8]
}

frame = pandas.DataFrame(my_stores)
print(frame)
