import logging

logging.basicConfig(filename="example.log", level=logging.DEBUG, format="%(asctime)s : %(levelname)s : %(message)s")

logging.debug("This is Information message")
logging.info("This is debug message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")

