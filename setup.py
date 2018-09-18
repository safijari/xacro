#!/usr/bin/env python
from setuptools import setup, find_packages

d = {}
d['name'] = 'xacro'
d['packages'] = find_packages()
d['scripts'] = ['scripts/xacro']

d['version'] = '1.13.3'

setup(**d)
