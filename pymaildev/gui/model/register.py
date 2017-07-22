#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""registre models"""

from pymaildev.gui import model  # __models__
from PyQt5.QtQml import qmlRegisterType


def registe_qml_models():
    """Registe model for import from *.qml"""
    for c in model.__models__:
        print("qml: reg " + c.__name__)
        qmlRegisterType(c, c.__name__, 1, 0, c.__name__)
