#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

#requirements = [ ]
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Matthew John Payne",
    author_email='matthewjohnpayne@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
    ],
    description="wis.py gives satellite positions at requested times. It manages kernel downloads. It requires astropy and spicepy. ",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='wis',
    name='wis',
    packages=find_packages(include=['wis']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/matthewjohnpayne/wis',
    version='1.0.0',
    zip_safe=False,
)
