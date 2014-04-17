import requests
from redis import Redis
from rq import Queue

def count_word_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())


