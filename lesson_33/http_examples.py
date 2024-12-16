import requests  # pip install requests

response = requests.delete("https://google.com/search",
                        params={"q": "big dogs"})
# query params


orig_req = response.request
print(orig_req)
print(f"Status code: {response.status_code}")
print(f"URL: {response.url}")
print(f"Content: \n {response.content}")

# API - application programing interface
