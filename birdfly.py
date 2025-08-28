import requests
import argparse
import os
import socket


parser = argparse.ArgumentParser(description='Scanner de Headers')
parser.add_argument('-u', '--url', help='Você precisa passar uma url com https://')
args = parser.parse_args()

url_web = args.url
if args.url:

	
	os.system("bash utils/banner.sh")
	domain = url_web.replace("https://", "").split()[0]

	res = requests.get(url_web)

	ip = socket.gethostbyname(domain)


	print(50*"-")
	print(f"[+] Powered by SEC-0 | Yumi and Marius Jabami")
	print(50*"-")

	print(f"Date: {res.headers['Date']}")
	print(f"Content Type: {res.headers['Content-Type']}")
	print(f"Server: {res.headers['Server']}")
	print(f"Connection: {res.headers['Connection']}")
	print(f"Cache Control: {res.headers['Cache-Control']}")
	print(f"X-XSS-PROTECTION: {res.headers['x-xss-protection']}")
	print(50*"-")
	print(f"IP: {ip}")
else:
	os.system('python birdfly.py -h')
