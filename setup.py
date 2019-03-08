#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import re
from setuptools import setup
from collections import OrderedDict

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

with io.open('alita/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='alita',
    version=version,
    url='https://github.com/dwpy/alita',
    project_urls=OrderedDict((
        ('Documentation', 'https://dwpy.github.io/alita'),
        ('Code', 'https://github.com/dwpy/alita'),
    )),
    license='BSD',
    author='Dongwei',
    description='A simple Python async framework for building web applications. ',
    long_description=readme,
    packages=[
        'alita',
        'alita.serve',
        'alita.contrib'
    ],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    python_requires='>=3.5',
    install_requires=[
        'bson',
        'attrs',
        'blinker',
        'click',
        'uvloop',
        'multidict',
        'itsdangerous',
        'httptools',
        'websockets',
        'gunicorn',
        'aiofiles',
    ],
    classifiers=[
        'Development Status :: Developing',
        'Environment :: Web Environment',
        'Framework :: Alita',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': [
            'alita = alita.contrib.command.cli:main',
        ],
    },
)
