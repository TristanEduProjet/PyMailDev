#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Model part of MVC app"""

from .email import Email
from .emailResume import EmailResume
from .account import Account
from .register import registeQmlModels

__all__ = ['email', 'emailResume', 'account', 'register']
__models__ = [Email, EmailResume, Account]
