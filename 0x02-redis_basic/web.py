#!/usr/bin/env python3

"""
This module defines a function to retrieve HTML content from a URL with caching and tracking.
"""


import requests
import redis
from functools import wraps


redis_client = redis.Redis()


def track_url_accesses(func):
    """
    Decorator to track how many times a particular URL was accessed.
    """
    @wraps(func)
    def wrapper(url):
        count_key = f"count:{url}"
        redis_client.incr(count_key)
        return func(url)
    return wrapper

def cache_page_result(expiration=10):
    """
    Decorator to cache the result of a function with a specified expiration time.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(url):
            cache_key = f"cache:{url}"
            cached_result = redis_client.get(cache_key)
            if cached_result:
                return cached_result.decode("utf-8")
            result = func(url)
            redis_client.setex(cache_key, expiration, result)
            return result
        return wrapper
    return decorator

@track_url_accesses
@cache_page_result()
def get_page(url: str) -> str:
    """
    Retrieve HTML content from a URL with caching and tracking.

    Args:
        url (str): The URL to retrieve HTML content from.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
