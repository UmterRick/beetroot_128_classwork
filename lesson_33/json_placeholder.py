from pprint import pprint
from unittest.mock import open_spec

import requests
import logging

from requests import HTTPError


PROTOCOL = "https://"
BASE_URL = "jsonplaceholder.typicode.com"

def make_request(method, url):
    try:
        response = requests.request(method, url) # method: "GET", "POST", "DELETE"
        response.raise_for_status()  # status_code >= 400
    except HTTPError as exc:
        logging.error(f"Request failed. Details: {exc.args}")
        raise exc


def get_all_posts() -> list[dict[str, ...]]:
    url = "/posts"
    final_url = PROTOCOL + BASE_URL + url
    logging.info(f"GET request to {final_url}")
    try:
        response = requests.get(final_url)
        response.raise_for_status() # status_code >= 400
    except HTTPError as exc:
        logging.error(f"Request failed. Details: {exc.args}")
        raise  exc
    return response.json()

def get_post_by_id(post_id):
    url = f"/posts/{post_id}"
    final_url = PROTOCOL + BASE_URL + url
    logging.info(f"GET request to {final_url}")
    try:
        response = requests.get(final_url)
        response.raise_for_status()  # status_code >= 400
    except HTTPError as exc:
        logging.error(f"Request failed. Details: {exc.args}")
        raise exc
    return response.json()


def create_new_post(new_post: dict):
    url = f"/posts"
    final_url = PROTOCOL + BASE_URL + url
    logging.info(f"POST request to {final_url}")
    try:
        response = requests.post(final_url, data=new_post)
        response.raise_for_status()  # status_code >= 400
    except HTTPError as exc:
        logging.error(f"Request failed. Details: {exc.args}")
        raise exc
    return response.json()


def edit_post(post_id, new_data):
    url = f"/posts/{post_id}"
    final_url = PROTOCOL + BASE_URL + url
    logging.info(f"PATCH request to {final_url}")
    try:
        response = requests.patch(final_url, data=new_data)
        response.raise_for_status()  # status_code >= 400
    except HTTPError as exc:
        logging.error(f"Request failed. Details: {exc.args}")
        raise exc
    return response.json()


def delete_post(post_id):
    url = f"/posts/{post_id}"
    final_url = PROTOCOL + BASE_URL + url
    logging.info(f"DELETE request to {final_url}")
    try:
        response = requests.delete(final_url)
        response.raise_for_status()  # status_code >= 400
    except HTTPError as exc:
        logging.error(f"Request failed. Details: {exc.args}")
        raise exc
    print(f"Delete Post#{post_id} status code: {response.status_code}")
    return response.json()


new_post = create_new_post(
    {
        "title": "My new post",
        "body": "Post body",
        "userId": 2
    }
)
# pprint(new_post)

# pprint(get_all_posts())

pprint(get_post_by_id(5))
print()
pprint(edit_post(5, {"title": "My title for post #5"}))
pprint(delete_post(5))


