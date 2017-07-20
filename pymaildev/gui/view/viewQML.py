#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Abstraction d'une vue QML"""

import sys
import os
import pymaildev
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

def start_qml(args, QmlController):
    """Démarre l'application en graphique"""
    app = QApplication(args)
    engine = QQmlApplicationEngine()
    ctx = engine.rootContext()  # QQmlContext
    engine.load(QmlController.__qml__)
    win = engine.rootObjects()[0]
    py_app = QmlController(ctx, win)
    # win.show()
    # sys.exit(app.exec())
    sys.exit(app.exec_())
