import logging
import json
from time import time

from memcache import Client
from scrapy.http import Headers
from scrapy.responsetypes import responsetypes
from scrapy.utils.request import request_fingerprint
from w3lib.http import headers_raw_to_dict, headers_dict_to_raw


logger = logging.getLogger(__name__)


class MemcachedCacheStorage:
    def __init__(self, settings):
        self.expiration_secs = settings.getint("HTTPCACHE_EXPIRATION_SECS")
        self.client = Client((settings["MEMCACHED_LOCATION"],))

    def key_for(self, spider, request, type_):
        """Creates unique identifiers to be used as cache keys in Memcached."""
        key = request_fingerprint(request)
        return "{}-{}-{}".format(spider.name, key, type_)

    def store_response(self, spider, request, response):
        """Store the given response in the cache."""
        meta_data = {
            "url": request.url,
            "method": request.method,
            "status": response.status,
            "response_url": response.url,
            "timestamp": time(),
        }
        data = (
            ("meta_data", json.dumps(meta_data)),
            ("response_headers", headers_dict_to_raw(response.headers)),
            ("response_body", response.body),
            ("request_headers", headers_dict_to_raw(request.headers)),
            ("request_body", request.body),
        )
        for type_, value in data:
            key = self.key_for(spider, request, type_)
            self.client.set(key, value, self.expiration_secs)

    def retrieve_response(self, spider, request):
        """Return response if present in cache, or None otherwise."""
        meta_data_key = self.key_for(spider, request, "meta_data")
        raw_meta_data = self.client.get(meta_data_key)
        meta_data = json.loads(raw_meta_data) if raw_meta_data else None
        if not meta_data:
            return

        body, raw_headers = (
            self.client.get(self.key_for(spider, request, type_))
            for type_ in ("response_body", "response_headers")
        )
        if not all((body, raw_headers)):
            return

        kwargs = {
            "url": meta_data.get("response_url"),
            "headers": Headers(headers_raw_to_dict(raw_headers)),
        }
        response_class = responsetypes.from_args(**kwargs)
        kwargs.update({"status": meta_data.get("status"), "body": body})
        return response_class(**kwargs)

    def open_spider(self, spider):
        logger.debug("Using memcached cache in", extra={"spider": spider})

    def close_spider(self, spider):
        pass
