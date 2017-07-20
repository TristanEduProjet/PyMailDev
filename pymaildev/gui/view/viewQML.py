#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Abstraction d'une vue QML"""

import sys
import os
import pymaildev
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import QUrl

__all__ = ['start_qml']

apps = []  # minimise the chances of crashe
# http://pyqt.sourceforge.net/Docs/PyQt5/gotchas.html#crashes-on-exit

def start_qml_(args, QmlController):
    """Démarre l'application en graphique"""
    global apps
    app=QGuiApplication(args)
    apps.append(app)
    # qml=QUrl()
    # assert qml.isValid()
    # print(qml.path())
    engine=QQmlApplicationEngine(QmlController.__qml__)
    engine.quit.connect(app.quit)
    engine.warnings.connect(warns)
    QmlController(engine.rootContext(), engine.rootObjects()[0])  # QQmlContext, QObject
    # sys.exit(app.exec())
    sys.exit(app.exec_())

def start_qml(args, QmlController):
    """Démarre l'application en graphique"""
    global apps
    app = QApplication(args)
    apps.append(app)
    engine = QQmlApplicationEngine(QmlController.__qml__)
    engine.quit.connect(app.quit)
    engine.warnings.connect(warns)
    QmlController(engine.rootContext(), engine.rootObjects()[0])  # QQmlContext, QObject
    # sys.exit(app.exec())
    sys.exit(app.exec_())

def warns(warnings):
    """Simple fonction de log pour l'app"""
    for w in warnings: print(w)
