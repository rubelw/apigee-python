#!/usr/bin/env python

from __future__ import absolute_import, division, print_function
from setuptools import setup, find_packages
import sys
from os import path
from io import open


DESCRIPTION = ("Apigee python client.")
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


VERSION = '0.0.4'

setup_requires = (
    ['pytest-runner'] if any(x in sys.argv for x in ('pytest', 'test', 'ptr')) else []
)

setup(
    name='apigee-python',
    version=VERSION,
    description=DESCRIPTION,
    url='https://github.com/rubelw/apigee-python',
    author='Will Rubel',
    author_email='willrubel@gmail.com',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    platforms=["any"],
    packages=find_packages(),
    include_package_data=True,
    setup_requires=setup_requires,
    tests_require=['pytest','mock'],
    test_suite="apigee-python.tests",
    install_requires=[
        "boto3>=1.4.3",
        "requests>=2.18",
        "Click>=6.7",
        "configparser>=3.5.0",
        "future>=0.16.0",
        "six>=1.11.0",
        "pip"
    ],
    keywords=['apigee', 'api', 'client'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)