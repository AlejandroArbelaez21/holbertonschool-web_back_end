#!/usr/bin/env python3
"""
Writing strings to Redis
"""
from redis import Redis
from uuid import uuid4


class Cache():
    """ Cache class """
    def __init__(self):
        """ store an instance of the Redis client as a private variable """
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        """ store the input data in Redis using the random key and return """
        random = str(uuid4())
        self._redis.set(random, data)
        return random
