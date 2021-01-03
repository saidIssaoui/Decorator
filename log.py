import logging
import os

class CustomFormatter(logging.Formatter):

    def format(self, record):
        if hasattr(record, 'func_name_override'):
            record.funcName = record.func_name_override
        if hasattr(record, 'file_name_override'):
            record.filename = record.file_name_override
        return super(CustomFormatter, self).format(record)


def get_logger():

    # Create logger object and set the format for logging and other attributes
    logger = logging.Logger(__name__)
    handler = logging.StreamHandler()
    logger.setLevel(logging.DEBUG)
    handler.setLevel(logging.DEBUG)
    logging.getLogger().setLevel(logging.DEBUG)
    handler.setFormatter(CustomFormatter('[%(asctime)s][file:%(filename)s]%(levelname)s [@%(funcName)s] %(message)s'))
    logger.addHandler(handler)

    # Return logger object
    return logger