#!/usr/bin/env python3

from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as readme:
    long_description = readme.read()

setup(
    name='Flask_Error',
    version='1.0.0',
    description='Easy error code and messages with useful troubleshooting and callback features.',
    long_description=long_description,
    url='https://github.com/Kiln707/Flask_Error',
    author='Kiln707',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='flask errors exceptions',
    packages=find_packages(),
    setup_requires='pytest-runner',
    tests_require=[
        'pytest',
        'pytest-cov'
    ],
    install_requires=[
        'flask'
    ],
    python_requires='>=3.5.*'
)
