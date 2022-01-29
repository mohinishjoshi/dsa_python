import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def log_event(self, msg, *value):
    if msg and value:
        logging.info(f'\n{msg}: {value}')
    elif msg:
        logging.info(f'\n{msg}')
    print("Current State -", self)