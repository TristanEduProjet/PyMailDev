#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Abstraction d'une vue QML"""

import os
import pymaildev
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtCore import QUrl, QSize, QDir

__all__ = ['start_qml']

apps = []  # minimise the chances of crashe
# http://pyqt.sourceforge.net/Docs/PyQt5/gotchas.html#crashes-on-exit

def start_qml_(args, QmlController):
    """Démarre l'application en graphique"""
    init_qml()
    global apps
    app=QGuiApplication(args)
    apps.append(app)
    setAppIcon(app)
    # app.setWindowIcon(QIcon(os.path.join(pymaildev.__resources__, "ico", "Wwalczyszyn-Mail.ico")))
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
    init_qml()
    global apps
    app = QApplication(args)
    apps.append(app)
    setAppIcon(app)
    # app.setWindowIcon(QIcon(os.path.join(pymaildev.__resources__, "ico", "Wwalczyszyn-Mail.ico")))
    engine = QQmlApplicationEngine()
    QmlController.init_pre_load(engine.rootContext())
    engine.load(QmlController.__qml__)
    engine.quit.connect(app.quit)
    engine.warnings.connect(warns)
    QmlController(engine.rootContext(), engine.rootObjects()[0])  # QQmlContext, QObject
    # sys.exit(app.exec())
    sys.exit(app.exec_())

def setAppIcon(app):
    """Modifie l'icône de l'application"""
    app_icon = QIcon()
    for s in (16, 24, 32, 48, 64, 72, 96, 128, 256):
        app_icon.addFile(os.path.join(pymaildev.__resources__, "ico", "Wwalczyszyn-Mail-{0}px.png".format(s)), QSize(s,s))
    app.setWindowIcon(app_icon)

def warns(warnings):
    """Simple fonction de log pour l'app"""
    for w in warnings: print(w)

def init_qml():
    """Initialise les variables de l'application"""
    QDir.addSearchPath("", os.path.join(pymaildev.__resources__, "qml"))
    QDir.addSearchPath("icons", os.path.join(pymaildev.__resources__, "icons"))
    # init_qml.func_code = (lambda:None).func_code  # trick only_once_called
    init_qml.__code__ = (lambda:None).__code__
