def write_logger_line(message):
    with open('logger.txt', 'a') as logger:
        logger.write(f'{message}\n')
    logger.close()
