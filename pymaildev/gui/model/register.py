#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import __init__
from PyQt5.QtQml import qmlRegisterType

def registeQmlModels():
    """Registe model for import from *.qml"""
    for c in __models__:
        print("qml: reg " + c.__name__)
        qmlRegisterType(c, c.__name__, 1, 0, c.__name__)
