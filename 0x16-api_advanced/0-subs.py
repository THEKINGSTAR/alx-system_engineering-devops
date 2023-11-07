#!/usr/bin/python3
"""
function that queries the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
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
        url_req = f'https://www.reddit.com/r/{subreddit}
                                    /about.json?limit={limit}&t={timeframe}'
        """
        headers = {'User-agent': 'yourbot'}
        url_req = f'https://www.reddit.com/r/{subreddit}/about.json'
        response = requests.get(url_req, headers=headers)

        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return (0)
    except Exception as e:
        # print(e)
        return (0)
