import logging
import datetime

logger=logging.getLogger("log in orange hrm")
current_time=datetime.datetime.now().strftime("%I-%M%p-%B-%d-%Y")
logpath="./logs/"+current_time

handler=logging.FileHandler(logpath+".log")
handler.setLevel(logging.DEBUG)

formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
handler.setFormatter(formatter)

logger.setLevel(level=logging.DEBUG)
logger.addHandler(handler)
