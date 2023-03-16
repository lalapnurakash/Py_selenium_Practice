import logging

logger=logging.getLogger(__name__)

filehandl=logging.FileHandler("sample.log",mode="w")
fm=logging.Formatter("%(asctime)s : %(levelname)s: %(name)s :%(message)s")
filehandl.setLevel(logging.DEBUG)
filehandl.setFormatter(fm)

logger.addHandler(filehandl)

logger.warning("hey warning")
logger.debug("this is debug")
logger.info("hey")
