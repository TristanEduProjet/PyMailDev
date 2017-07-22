#!/bin/python
# -*- coding: utf-8 -*-

"""
Package principal du programme.

Voir le readme ou le dépôt Git pour plus d'information.
"""

__version__ = '0.1.5'
__fullname__ = 'PyMailDev'

# from pkg_resources import resource_string, resource_listdir
# print resource_listdir('proj.resources.images', '')
# print resource_string('proj.resources.images', 'pic2.png').encode('base64')
__resources__ = __import__('os').path.join(
    __import__('os').path.dirname(__import__('os').path.abspath(__file__)),
     "resources")
