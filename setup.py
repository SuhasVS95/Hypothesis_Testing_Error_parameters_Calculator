# -*- coding: utf-8 -*-
"""
Created on Sat May 1 19:45:08 2021

@author: Suhas V S
"""

from setuptools import setup
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


VERSION = '0.0.4'
DESCRIPTION = 'Calculate the parameters of the power of a test in Hypothesis Testing iteratively'


setup(
    name="error_param_cal",
    version=VERSION,
    author="Suhas V S",
    author_email="<suhas95vs@gmail.com>",
    long_description=README,
    long_description_content_type="text/markdown",
    #url="https://github.com/kishore-s-gowda/fastreport",
    license="MIT",
    keywords=['python', 'sample_size', 'Type I Error', 'Type II Error'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    py_modules = ['error_param']
)
