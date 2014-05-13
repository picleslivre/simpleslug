#!/usr/bin/env python
import sys
import re
from setuptools import setup, Extension

import simpleslug


version = simpleslug.__version__

setup(
    name="simpleslug",
    version=version,
    description="Generates slug strings for given strings.",
    author="Fabio Batalha",
    author_email="fabiobatalha@gmail.com",
    license="BSD 2-Clause",
    url="http://github.com/picleslivre/simpleslug/",
    py_modules=["simpleslug"],
    tests_require=tests_require,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    test_suite="tests",
)
