import logging
import sys
import pandas

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

logging.info('-----------------------------')
logging.info('processing script test pandas')
logging.info('-----------------------------\n')

my_stores = {
    'stores': [
        'Supermercado BH',
        'Supermercado NC',
        'Supermercado 12',
        'Supermercado 134',
        'Supermercado 34',
        'Supermercado 67'
    ],
    'counters': [
        78,
        8,
        23,
        86,
        89,
        10
    ]
}

frame = pandas.DataFrame(my_stores)

print(frame)
logging.info('-----------------------------\n')
print(frame['stores'])
logging.info('-----------------------------\n')
print(frame.describe())
logging.info('-----------------------------\n')
print(frame.sort_values(by='counters'))
