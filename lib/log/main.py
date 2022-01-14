import logging
logger = logging.getLogger("Xbox-Spam") 


def console(message):
	ch = logging.StreamHandler()
	logger.addHandler(ch)
	logger.setLevel(logging.INFO)
	ch.setLevel(logging.INFO)
	logger.info(message)
    
class colors:
	grey = "\033[1;38;40m"
	yellow = "\033[1;33;40m"
	red = "\033[1;31;40m"
	blue = "\033[1;34;40m"
	green = "\033[1;32;40m"
	reset = "\033[0m"
	critical = "\033[1;37;41m"


def consoleColor(color, signal, message):
	msg = "%s[%s] %s %s" % (color, signal, message, colors.reset)
	return print(msg)

def defaultConfiguration(type, message):
	if len(type) < 1:
		raise TypeError("Please provide a type of message")
	if type == 'sucess':
		return consoleColor(colors.green, '+',  message)
	elif type == 'alert':
		return consoleColor(colors.blue, '*', message)
	elif type == 'unsucess':
		return consoleColor(colors.red, '-', message)
	elif type == 'warning':
		return consoleColor(colors.yellow, '!', message)
	elif type == 'critical':
		return consoleColor(colors.critical, 'CRITICAL', message)
