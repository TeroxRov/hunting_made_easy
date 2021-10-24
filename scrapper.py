import argparse
import requests
import os

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url',type=str,help="url to get its response")
args = parser.parse_args()
url = args.url
request = requests.get(args.url)
print(args.url,' :: ',request)

