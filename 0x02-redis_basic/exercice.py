#!/usr/bin/env python3

"""
This module defines a Cache class for storing and retrieving data
"""
import sys
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps

class Cache:
    """
    A class for caching data in Redis with conversion options.
    """

    def __init__(self) -> None:
        """
        Initialize the Cache object with a Redis client and flush the instance.
        """
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        """
        Decorator to count the number of times a method is called.

        Args:
            method (Callable): The method to be decorated.

        Returns:
            Callable: The decorated method.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    @staticmethod
    def call_history(method: Callable) -> Callable:
        """
        Decorator to store the history of inputs and outputs for a particular function.

        Args:
            method (Callable): The method to be decorated.

        Returns:
            Callable: The decorated method.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            inputs_key = method.__qualname__ + ":inputs"
            outputs_key = method.__qualname__ + ":outputs"
            self._redis.rpush(inputs_key, str(args))
            result = method(self, *args, **kwargs)
            self._redis.rpush(outputs_key, str(result))
            return result
        return wrapper

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store input data in Redis using a random key and return the key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored in the cache.

        Returns:
            str: The random key used to store the data in Redis.
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis with the given key and optionally convert it using the provided function.

        Args:
            key (str): The key used to retrieve data from the cache.
            fn (Optional[Callable]): A function to convert the retrieved data.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data, optionally converted by fn.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data
    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve data from Redis with the given key and convert it to a string.

        Args:
            key (str): The key used to retrieve data from the cache.

        Returns:
            Union[str, None]: The retrieved data as a string, or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve data from Redis with the given key and convert it to an integer.

        Args:
            key (str): The key used to retrieve data from the cache.

        Returns:
            Union[int, None]: The retrieved data as an integer, or None if the key does not exist.
        """
        return self.get(key, fn=int)
