#!/usr/bin/python3
"""
function that queries the Reddit API
"""

import json
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API
    and
    prints the titles of the first 10 hot posts listed for a given subreddi
    """
    try:
        """
        about = 'about'
        limit = 10
        timeframe = 10
        timeframe = hour, day, week, month, year, all
        listing = controversial, best, hot, new, random, rising, top

        'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={count}&t={timeframe}'

        url_req = f'https://www.reddit.com/r/{subreddit}
                                    /about.json?limit={limit}&t={timeframe}'
        """
        listing = 'top'
        limit = 10
        timefrm = 'all'
        headers = {'User-agent': 'yourbot'}
        redit = 'https://www.reddit.com/r/'
        sub = subreddit
        url_req = f'{redit}{sub}/{listing}.json?limit={limit}&t={timefrm}'

        response = requests.get(url_req, headers=headers)

        if response.status_code == 200:
            data = response.json()
            top = data['data']['children']
            posts = []
            for post in data['data']['children']:
                x = post['data']['title']
                print(x)
                posts.append(x)
            # print(posts)
        else:
            print(None)
    except Exception as e:
        # print(e)
        return (0)
