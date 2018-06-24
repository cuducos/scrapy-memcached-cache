from setuptools import setup

with open("README.rst") as fobj:
    long_description = fobj.read()

setup(
    author="Eduardo Cuducos",
    author_email="cuducos@gmail.com",
    classifiers=(
        "Development Status :: 4 - Beta",
        "Environment :: Plugins",
        "Framework :: Scrapy",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
    ),
    description="Memcached HTTP cache storage backend for Scrapy",
    install_requires=("scrapy", "python-memcached"),
    long_description=long_description,
    name="scrapy-memcached-cache",
    py_modules=["scrapy_memcached_cache"],
    url="https://github.com/cuducos/scrapy-memcached-cache",
    version="0.0.3",
    zip_safe=False,
)
