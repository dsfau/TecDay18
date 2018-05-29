from faker import Faker
import requests
import hashlib
gen = Faker()
hsh = hashlib.sha1()
def ids():
	for i in range(0,200):
		payload={'id' : gen.random_number()}
		r=requests.get("http://82.223.66.86/index.php", params=payload)
def notices():
	for i in range(0,200):
		payload={'notice' : gen.sentence().replace(" ", "_")}
		r=requests.get("http://82.223.66.86/index.php", params=payload)
def usernames():
	for i in range(0,200):
		p = gen.profile()
	        payload={'username' : p['username'], 'password': hashlib.sha1(str(gen.random_number())).hexdigest(), 'email': p['mail']}
		payload1={'username':p['username']}
	        r=requests.post("http://82.223.66.86/index.php", params=payload)
		r1=requests.get("http://82.223.66.86/index.php", params=payload1)
for i in range(0,100):
	sorteo =  gen.random_number()%2
	if sorteo == 0:
		usernames()
	if sorteo == 1:
		ids()
	if sorteo == 2:
		notices()
