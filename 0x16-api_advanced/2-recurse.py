#!/usr/bin/python3
"""
function that queries the Reddit API
"""

import json
import requests


def recurse(subreddit, hot_list=[]):
    """
    returns the number of subscribers (not active users, total subscribers)
    for a given subreddit.
    If an invalid subreddit is given, the function should return 0
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
            for post in data['data']['children']:
                x = post['data']['title']
                # print(x)
                hot_list.append(x)
            return (hot_list)
        else:
            return (None)
    except Exception as e:
        # print(e)
        return (0)
