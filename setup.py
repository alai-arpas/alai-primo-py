try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import oratabss

with open("README.md") as readme_file:
    readme_string = readme_file.read()

setup(
    version=oratabss.__version__,
)
