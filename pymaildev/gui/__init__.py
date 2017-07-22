#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Partie graphique de l'application

Lib utilisée: pyform
"""

from .model import *
# from .view import *
from .view import start_qml
# from .controller import *
from .controller import MainController, MailController, AccountParamsController

__all__ = ['model', 'view', 'controller']
