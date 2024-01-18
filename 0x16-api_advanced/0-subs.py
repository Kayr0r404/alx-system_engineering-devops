#!/usr/bin/python3
''' Api'''
import requests


def number_of_subscribers(subreddit):
    '''get number of subcribers subcribed to the provided subreddit'''
    try:
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        headers = {'user-agent': 'my-app/0.0.1'}
        response = requests.get(url, headers=headers)
        if response.status_code == 400:
            return 0
        else:
            return response.json()['data']['subscribers']
    except Exception as e:
        pass
        return 0
