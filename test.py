import requests
import urllib3

print("TESTING")

r=requests.get("https://pikfrank.osisoft.int/piwebapi")
print(r.status_code)