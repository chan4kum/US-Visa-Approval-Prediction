from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys


logging.info("Welocome to out custom log")

try:
    a=1/"10"

except Exception as e:
    raise USvisaException(e,sys) from e