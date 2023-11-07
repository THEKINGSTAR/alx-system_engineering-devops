#!/usr/bin/python3
"""
Function that queries the Reddit API
"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers (not active users, total subscribers)
    for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    try:
        # Use the correct API endpoint for subreddit information
        url_req = f'https://www.reddit.com/r/{subreddit}/about.json'
        headers = {'User-agent': 'yourbot'}
        response = requests.get(url_req, headers=headers)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            # If the response status code is not 200, return 0
            return 0
    except Exception as e:
        # Handle exceptions gracefully
        print(f"An error occurred: {e}")
        return 0

# Example usage:
subreddit_name = 'python'
subscribers_count = number_of_subscribers(subreddit_name)
print(f"Subscribers of r/{subreddit_name}: {subscribers_count}")
