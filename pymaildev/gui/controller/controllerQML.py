#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Abstraction d'un controlleur QML"""

import os
import pymaildev
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon


class ControllerQML(QObject):
    """Abstract QML controller"""

    def __init__(self, context, parent=None):
        """..."""
        # super(type(self), self).__init__(parent)
        super().__init__(parent)
        self.win = parent
        self.ctx = context
        # self.win.setIcon(QIcon(os.path.join(pymaildev.__resources__, "ico", "Wwalczyszyn-Mail.ico")))
        self.ctx.setContextProperty("pyController", self)
        self.win.show()
        self.init_post_load()

    @staticmethod
    def init_pre_load(context):
        """Called before load qml"""
        pass

    # @staticmethod
    def init_post_load(self):
        """Call after load qml"""
        pass
