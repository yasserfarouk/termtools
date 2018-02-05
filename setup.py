#!/usr/bin/env python
"""
setup file.

Uses pipenv to get dependencies not requirements.txt.
"""
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='yutils',
    version='0.1.8',
    description='A collection of utility functions/decorators/classes I use',
    long_description=long_description,
    url='https://github.com/yasser/yutils',
    author='Yasser Mohammad',
    author_email='yasserfarouk@gmail.com',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
    ],
    keywords='utilities',
    packages=find_packages(),
    install_requires=['numpy', 'scipy', 'pandas', 'arff'],
    python_requires='>3.6',
    install_package_data=False,
)
