from __future__ import with_statement

try:
    from setuptools import setup
except:
    from distutils.core import setup

import haikunator

haikunator_classifiers = [
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]

with open('README.rst', 'r') as fp:
    haikunator_long_description = fp.read()

setup(name='pyhaikunator',
      version=haikunator.__version__,
      author='Ferhat Elmas',
      author_email='elmas.ferhat@gmail.com',
      url='https://github.com/ferhatelmas.pyhaikunator',
      py_modules=['haikunator'],
      license='MIT',
      description='Heroku like random name generator',
      long_description=haikunator_long_description,
      classifiers=haikunator_classifiers
)
