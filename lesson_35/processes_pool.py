import time
from multiprocessing import Pool


def handle_request(url):
    print(f"Send requests to {url}")
    time.sleep(1)
    return f"Response from {url}"


with Pool(5) as pool:
    urls = [
        "a",
        "b",
        "c",
        "d",
        "f",
        "e",
        "g",
        "h",
    ]
    results = pool.map(handle_request, urls)
    print("Responses", results)