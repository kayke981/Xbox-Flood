from requests import Session, Request
from lib.log.main import console, colors, defaultConfiguration
from lib.header.header import agent
import json
import threading
import random
import os

s = Session()

def request(method, path, headers, payload):
	BaseUrl = 'https://xbl.io/api/v2'
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
def search(namertag, key):
	headers = {}
	headers["X-Authorization"] = key
	data = request('GET', '/friends/search?gt=' + namertag, headers, payload = {})
	
	if data.status_code != 200:
		raise TypeError(data.text)
		pass
	xuid = data.json()["profileUsers"][0]["id"]
	defaultConfiguration('sucess', 'Xuid successfully found of %s (%s)' % (namertag, xuid))
	return xuid
def send_message(xuid, message, key, b):
	headers = {} 
	headers["X-Authorization"] = key
	headers["User-Agent"] = agent()
	headers["Connection"] = 'keep-alive'
	headers["Keep-Alive"] = str(random.randint(110,120))
	payload = {}
	payload["xuid"] = xuid
	payload["message"] = message
	res = request('POST', '/conversations', headers, payload)
	if res.text == None:
		defaultConfiguration('error', 'Message not sent, an error occurred')
	defaultConfiguration('sucess', 'Message sent successfully')
def menu():
	key = input('Put your key here: ')
	print('1) - Spam messages'.center(50, ' '))
	print('2) - Update'.center(43, ' '))
	choice = input('Select an option: ')
	if choice == '1':
		amount = input('How many messages do you want to send?: ')
		namertag = input('Put the namertag: ')
		message = input('What message do you want to send?: ')
		defaultConfiguration('alert', 'Starting...')
		defaultConfiguration('alert', "Finding xuid of %s..." % (namertag))
		xuid = search(namertag, key)
		defaultConfiguration('alert', "Preparing... Sending message to %s (%s)" % (namertag, xuid))
		for b in range(int(amount)):
			t = threading.Thread(target=send_message, args=(xuid, message, key, b))
			t.deamon = True
			t.start()
	if choice == '2':
		defaultConfiguration('alert', 'Starting pull request...')
		defaultConfiguration('alert', "Executing 'git pull'")
		os.system('git pull')
		defaultConfiguration('sucess', 'Done...')
def main():
	print(colors.yellow + "[!] If you mess up, it's all your problem" + colors.reset)
	defaultConfiguration('alert', 'Starting the menu...')
	menu()
try:
	main()
except KeyboardInterrupt:
	pass
