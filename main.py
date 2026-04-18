import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = RotatingFileHandler('log.txt', maxBytes=1024*1024*10, backupCount=5)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def main():
    logger.debug('Dastur ishga tushdi')
    try:
        x = 5 / 0
    except ZeroDivisionError:
        logger.error('Nolga bo\'lish xatosi')
    logger.info('Dastur tugadi')

if __name__ == '__main__':
    main()
    logger.critical('Dastur tugadi')