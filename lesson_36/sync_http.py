import time

import requests


def fetch_data(url):
    response = requests.get(url)
    return response.text


def main():
    base_url = "https://jsonplaceholder.typicode.com/posts/"
    for i in range(1, 101):
        fetch_data(base_url + str(i))


start = time.time()
main()
print(f"Time: {time.time() - start} s")
