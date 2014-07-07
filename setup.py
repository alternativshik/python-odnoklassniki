#!/usr/bin/env python
from distutils.core import setup

setup(
    name='odnoklassniki',
    version='0.9.1',
    description='Odnoklassniki API wrapper for python',
    author='Sergey Maltsev',
    author_email='alternativshik@gmail.com',
    url='https://github.com/alternativshik/python-odnoklassniki',
    download_url='https://pypi.python.org/pypi/odnoklassniki/',
    install_requires=[
        'requests'
    ],
    packages=[
        'odnoklassniki',
    ]
)
