import requests
import sys
import argparse
import json

parser = argparse.ArgumentParser()
# parser.add_argument('arguments', nargs="+", help="Give the arguments")
parser.add_argument('arguments', nargs="*", help="Give the arguments")
parser.add_argument("--category", "--category", help="Give the category")
parser.add_argument("--filetype", "--filetype", help="Give the file name with type")

args = parser.parse_args()

URL = "http://tomcat01.production2.telyportal.com:9080/"
fileList = []
if args.arguments:
	if args.arguments[0] == "list":
		reqType = "GET"
		URL =  URL + "dataset"
		if args.category:
			URL = URL + "?category=" + args.category
	elif args.arguments[0] == "search":
		reqType = "GET"
		URL = URL + "dataset/?q=" + args.arguments[1].replace(' ','+')
	elif args.arguments[0] == "add":
		reqType = "POST"
		URL = URL + "filetype/"
		if args.filetype:
			fileList.append(args.filetype)
		elif len(args.arguments) > 1:
			fileList = args.arguments[1:]
		else:
			print("Please provide filetype")
			exit()
	else:
		print ("Please provide right command")
		exit()
else:
    print ("No command provided")
    exit()

if reqType == "GET":
	response = requests.get(url = URL).json()
	print(response)
elif reqType == "POST":
	for file in fileList:
		f = open(file, 'r')
		data = f.read()
		f.close()
		response = requests.post(url = URL, data = data, headers = {"Content-Type": "application/json"})
		print(response.status_code, response.reason, response.json())