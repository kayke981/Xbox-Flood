from requests import Session, Request
from lib.log.main import console, colors
from lib.header.header import agent
import json
import time
import threading

def request(method, path, headers, payload):
	BaseUrl = 'https://xbl.io/api/v2'
	s = Session()
	url = BaseUrl + path
	user_agent = agent()
	headers["User-Agent"] = user_agent
	headers["Accept"] = 'application/json'
	headers["Content-Type"] = 'aplication/json'
	headers["Accept-Language"] = "en-US"
	req = Request(method, url, headers=headers, data=json.dumps(payload))
	pp = req.prepare()
	res = s.send(pp)
	return res
def search(namertag, key, b):
	headers = {}
	headers["X-Authorization"] = key
	data = request('GET', '/friends/search?gt=' + namertag, headers, payload = {})
	try:
		msg = colors.green + '[+]' + colors.reset + colors.white + ' Xuid successfully found' + colors.reset
		if b == 0:
			console(msg)
		return data.json()["profileUsers"][0]["id"]
	except:
		pass
def send_message(namertag, message, key, b):
	xuid = search(namertag, key, b)
	headers = {} 
	headers["X-Authorization"] = key
	payload = {}
	payload["xuid"] = xuid
	payload["message"] = message
	res = request('POST', '/conversations', headers, payload)
	# print(res.text)
	try:
		if res.json()["message"] == 'Invalid API Key.':
			raise TypeError(colors.bold_red + 'Error: Your api key is invalid' + colors.reset)
	except:
		pass
	if res.status_code != 200:
		msgError = colors.red + '[!]' + colors.reset + colors.white + ' Message not sent, an error occurred' + colors.reset
		print(msgError)
	elif res.status_code == 200:
		msgSuccess = colors.green + '[+]' + colors.reset + colors.white + ' Message sent successfully' + colors.reset
		print(msgSuccess)
def menu():
	key = input('Put your key here: ')
	print('1) - Spam messages'.center(50, ' '))
	choice = input('Select an option: ')
	if choice == '1':
		amount = input('How many messages do you want to send?: ')
		namertag = input('Put the namertag: ')
		message = input('What message do you want to send?: ')
		for b in range(int(amount)):
			t = threading.Thread(target=send_message, args=(namertag, message, key, b))
			t.daemon = True
			t.start()
def main():
	print(colors.yellow + "[!] If you mess up, it's all your problem" + colors.reset)
	print(colors.green + '[+] Starting the menu...' + colors.reset)
	menu()
main()