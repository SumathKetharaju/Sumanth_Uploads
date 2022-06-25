import requests

payload = {"page": 2, "count": 25}

response = requests.get("https://httpbin.org/get", params=payload)

print(response.text)

"""
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.27.1", 
    "X-Amzn-Trace-Id": "Root=1-624d054b-1df9404d66595fe53578e656"
  }, 
  "origin": "117.195.212.85", 
  "url": "https://httpbin.org/get"
}
"""
