import requests
# import time


# for _ in range(15):
#     response = requests.get("https://www.cloudflare.com/rate-limit-test/")

#     print(response.status_code)

#     time.sleep(6)

try:
    response = requests.get("http://httpbin.org/delay/10", timeout=2)
except requests.Timeout:
    response = requests.get("http://httpbin.org/delay/10", timeout=15)
finally:
    print(response.status_code)