#!/bin/python
# -*- coding: utf-8 -*-

"""
Main program's package

For more informations, see the README.md file, or the GitHub repository
"""

__version__ = '0.1.5'
__fullname__ = 'PyMailDev'

# from pkg_resources import resource_string, resource_listdir
# print resource_listdir('proj.resources.images', '')
# print resource_string('proj.resources.images', 'pic2.png').encode('base64')
__resources__ = __import__('os').path.join(
    __import__('os').path.dirname(__import__('os').path.abspath(__file__)),
    "resources")
