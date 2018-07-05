#__author__ QILIN YOU

import requests
import re

def GetPublicIP():
	url = 'http://checkip.dyndns.com/'
	info = requests.get(url).text
	return re.compile(r'IP Address: (\d+.\d+.\d+.\d+)').search(info).group(1)

def Location(data):

	city = re.compile(r'city: ([^,]+)').search(data).group(1)
	region = re.compile(r'region: ([^,]+)').search(data).group(1)
	country =  re.compile(r'country: ([^,]+)').search(data).group(1)
	location =  re.compile(r'loc: ([^,]+)').search(data).group(1)
	address = dict(city = city, region = region, country = country, location = location)
	return address
if __name__ == "__main__":
	# Get Public IP
	Public_IP = GetPublicIP()

	url = 'https://ipinfo.io/' + Public_IP + '/json'
	data = requests.get(url).text.replace('"',"")
	# extract info
	Address = Location(data)

	print(Address['city'])