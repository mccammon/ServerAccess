#!/usr/bin/env python3

import os
import re
from setuptools import setup

ROOT = os.path.dirname(__file__)

def read_file(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='ServerAccess',
    version='0.0.1',
    author='Scott McCammon',
    packages=['ServerAccess'],
    long_description=read_file('README.md'),
    install_requires=required,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Natural Language :: English"
    ]
)