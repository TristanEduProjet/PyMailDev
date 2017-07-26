#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module configuration serveur mail

Utils pour la configuration du serveur de mail
"""

from enum import Enum, IntEnum


TypeSend = Enum('TypeSend', 'SMTP')

TypeReceive = Enum('TypeReceive', 'POP3 IMAP')


# TypeSecurity = Enum('TypeSecurity', 'NONE StartTLS SSL')
class TypeSecurity(Enum):
    """..."""

    NONE = 'none'
    StartTLS = 'strattls'
    SSL = 'ssl'
    TLS = 'tls'
