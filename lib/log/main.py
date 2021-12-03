import logging
logger = logging.getLogger("Xbox-Spam") 


def console(message):
	ch = logging.StreamHandler()
	logger.addHandler(ch)
	logger.setLevel(logging.INFO)
	ch.setLevel(logging.INFO)
	logger.info(message)
    
class colors:
  grey = "\x1b[38m" 
  yellow = "\x1b[33m" 
  red = "\x1b[31m" 
  bold_red = "\x1b[31;1m" 
  reset = "\x1b[0m"
  bold = "\x1b[1m"
  blue = "\x1b[94m"
  cyan = "\x1b[96m"
  dark_cyan = "\x1b[36m"
  white = "\x1b[m"
  green = "\x1b[92m"