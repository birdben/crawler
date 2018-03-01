import requests

proxies = {
  "http": "http://117.90.2.34:9000"
}

r = requests.get("https://github.com/timeline.json", proxies=proxies)

print(r.json())
