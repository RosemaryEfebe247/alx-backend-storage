#!/usr/bin/env python3
""" A class object that generates a UUID for a data
returns the UUID(key) of the data
"""
import redis
import uuid
from typing import Callable, Union


class Cache:
    def __init__(self, host='localhost', port=6379, db=0):
        """ Iniitialization of the init function
        Args:
            host: The host of the redis which is set ti a default
            port: port number set to a default
            db: The database storage
        """
        self._redis = redis.Redis(host=host, port=port,
                                  db=db, decode_responses=True)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ This method takes a data argument
        returns a string of UUID genrated key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """ Get data and convert to fn if fn not none"""
        data = self._redis.get(key)
        if fn is not None and data is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """ Automatically parametrize Cache.get
        with the correct conversion function (str)"""
        return self.get(key, fn=str)

    def get_int(self, key: str) -> Union[int, None]:
        """ Automatically parametrize Cache.get
        with the correct conversion function (int)"""
        return self.get(key, fn=int)
