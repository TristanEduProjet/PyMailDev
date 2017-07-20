#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Abstraction d'un controlleur QML"""

from PyQt5.QtCore import QObject

class ControllerQML(QObject):
    """Abstract QML controller"""

    def __init__(self, context, parent=None):
        # super(type(self), self).__init__(parent)
        super().__init__(parent)
        self.win = parent
        self.ctx = context
        self.ctx.setContextProperty("pyController", self)
        self.win.show()
