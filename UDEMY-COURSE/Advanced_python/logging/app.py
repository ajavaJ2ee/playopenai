import logging
logging.basicConfig(format='%(asctime)s %(levelname)-8s:[%(filename)s:%(lineno)d] %(message)s'
                    , level=logging.DEBUG
                    , filename='logs.txt')

logger= logging.getLogger('test-logger')


logger.debug('Say Hi from DEBUG')

logger.info('Say Hi from Info')

logger.warning('Say Hi from Warning')
