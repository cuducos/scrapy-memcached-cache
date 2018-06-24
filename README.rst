.. image:: https://img.shields.io/travis/cuducos/scrapy-memcached-cache.svg
   :alt: Travis
   :target: https://travis-ci.org/cuducos/scrapy-memcached-cache

.. image:: https://img.shields.io/pypi/v/scrapy-memcached-cache.svg
   :alt: PyPI
   :target: https://pypi.org/project/scrapy-memcached-cache/

Scrapy Memcached Cache
======================

Memcached HTTP cache storage backend for `Scrapy <https://scrapy.org/>`_.

Install
-------

Install the package with ``pipenv install scrapy-memcached-cache`` or ``pip install memcached-cache``.

Usage
-----

In your Scrapy ``settings.py``:

1. Enable HTTP cache with ``HTTPCACHE_ENABLED = True``
2. Set the cache expiration (in seconds), for example, with ``HTTPCACHE_EXPIRATION_SECS = 600``
3. Set ``MemcachedCacheStorage`` as your cache storage with ``HTTPCACHE_STORAGE = 'scrapy_memcached_cache.MemcachedCacheStorage'``
4. Set the location where your Memcached is running, for example, with ``MEMCACHED_LOCATION=localhost:11211``
5. Done 🎉

Contributing
------------

Please, format your code with `Black <https://github.com/ambv/black>`_.