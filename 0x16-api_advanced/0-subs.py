#!/usr/bin/python3
''' Api'''
import requests


def number_of_subscribers(subreddit):
    '''get number of subcribers subcribed to the provided subreddit'''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'linux:0x16.api.advanced:v1.0.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    else:
        return response.json()['data']['subscribers']
