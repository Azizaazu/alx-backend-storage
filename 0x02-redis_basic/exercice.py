#!/usr/bin/env python3

"""
This module defines a Cache class for storing and retrieving data
"""


import sys
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


UnionOfTypes = Union[str, bytes, int, float]


class Cache:
    """
    A class for caching data in Redis with conversion options.
    """

    def __init__(self):
        """
        Initialize the Cache object with a Redis client and flush the instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def count_calls(method: Callable) -> Callable:
        """
        Decorator to count the number of times a method is called.

        Args:
            method (Callable): The method to be decorated.

        Returns:
            Callable: The decorated method.
        """
        key = method.__qualname__


        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """ wrap """
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    def call_history(method: Callable) -> Callable:
        """
        Decorator to store the history of inputs and outputs for a particular function.

        Args:
            method (Callable): The method to be decorated.

        Returns:
            Callable: The decorated method.
        """
         key = method.__qualname__
    i = "".join([key, ":inputs"])
    o = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapp """
        self._redis.rpush(i, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(o, str(res))
            return res
        return wrapper

    @count_calls
    @call_history
    def store(self, data: UnionOfTypes) -> str:
        """
        Store input data in Redis using a random key and return the key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored in the cache.

        Returns:
            str: The random key used to store the data in Redis.
        """
        key = str(uuid4())
        self._redis.mset(key: data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> UnionOfTypes:
        """
        Retrieve data from Redis with the given key and optionally convert it using the provided function.

        Args:
            key (str): The key used to retrieve data from the cache.
            fn (Optional[Callable]): A function to convert the retrieved data.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data, optionally converted by fn.
        """
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_int(self: bytes) -> int:
        """get a number"""
        return int.from_bytes(self, sys.byteorder)

    def get_str(self: bytes) -> str:
        """get a string"""
        return self.decode("utf-8")
