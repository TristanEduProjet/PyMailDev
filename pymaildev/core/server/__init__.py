#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Configuration serveur mail

Utils pour la configuration du serveur de mail
"""

from .types import *
from .MailServer import ServerConf, ServerAutoConf

__all__ = ['MailServer', 'types']
