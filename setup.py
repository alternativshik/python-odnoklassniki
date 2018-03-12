#!/usr/bin/env python
from distutils.core import setup

setup(
    name='odnoklassniki',
    version='1.0',
    description='Odnoklassniki API wrapper',
    author='Serhii Maltsev',
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
