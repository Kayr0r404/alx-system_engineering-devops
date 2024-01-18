#!/usr/bin/python3
''' Api'''
import requests


def number_of_subscribers(subreddit):
    '''get number of subcribers subcribed to the provided subreddit'''
    try:
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['data']['subscribers']
        else:
            return 0
    except Exception as e:
        print('Error:', e)
        return 0
