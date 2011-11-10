"""
setup.py for jira-cli
"""
__author__ = "Ali-Akber Saifee"
__email__ = "ali@indydevs.org"

import os
import sys
from setuptools import setup, find_packages, Command


setup(name='jiracli',
     version = "0.1",
     description = "command line utility for interacting with jira",
     long_description = "",
     packages = find_packages(exclude=['ez_setup']),
     include_package_data = True,
     zip_safe = False,
     install_requires =[
         'setuptools',
         'termcolor'
         ],
     entry_points = {
         'console_scripts' : [
             'jiracli = jiracli.cli:main',
             ]
        },
     )

