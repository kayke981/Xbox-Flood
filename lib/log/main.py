import logging
logger = logging.getLogger("Xbox-Spam") 


def console(message):
	ch = logging.StreamHandler()
	logger.addHandler(ch)
	logger.setLevel(logging.INFO)
	ch.setLevel(logging.INFO)
	logger.info(message)
    
class colors:
  grey = "\x1b[38;1m" 
  yellow = "\x1b[33m" 
  red = "\x1b[31m" 
  bold_red = "\x1b[31;1m" 
  reset = "\x1b[0m"
  bold = "\x1b[1m"
  blue = "\x1b[94m"
  cyan = "\x1b[96;1m"
  dark_cyan = "\x1b[36m"
  white = "\x1b[m"
  green = "\x1b[92;1m"

def consoleColor(color, signal, message):
	msg = "%s[%s%s%s%s]%s %s" % (colors.grey, color, signal, colors.reset, colors.grey, colors.reset, message)
	return print(msg)

def defaultConfiguration(type, message):
	if len(type) < 1:
		raise TypeError("Please provide a type of message")
	if type == 'sucess':
		return consoleColor(colors.green, '+',  message)
	elif type == 'alert':
		return consoleColor(colors.blue, '*', message)
	elif type == 'unsucess':
		return consoleColor(colors.bold_red, '-', message)
	elif type == 'warning':
		return consoleColor(colors.yellow, '!', message)