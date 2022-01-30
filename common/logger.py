import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def log_event(self, msg, *value):
    if msg and value:
        logging.info(msg, str(value))
    elif msg:
        logging.info(msg)