#!/usr/bin/env python3
""" A class object that generates a UUID for a data
returns the UUID(key) of the data
"""
import redis
import uuid
from typing import Union


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
