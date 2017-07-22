#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtProperty
from .emailResume import EmailResume

class Email(EmailResume):
    """Email complete model"""

    def __init__(self, parent=None):
        super().__init__(parent)

    @pyqtProperty('QString')
    @property
    def to(self):
        return self._to

    @to.setter
    def to(self, to):
        self._to = to

    @pyqtProperty('QString')
    @property
    def cc(self):
        return self._cc

    @cc.setter
    def cc(self, cc):
        self._cc = cc

    @pyqtProperty('QString')
    @property
    def cci(self):
        return self._cci

    @cci.setter
    def cci(self, cci):
        self._cci = cci

    @pyqtProperty('QString')
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    @staticmethod
    def create(ffrom, to, cc, cci, subject, message, parent=None):
        """Create object mail from existing data"""
        mail = Email(parent)
        mail.of(ffrom)
        mail.to(to)
        mail.cc(cc)
        mail.cci(cci)
        mail.subject(subject)
        mail.message(message)
        return mail

    def __str__(self):
        """Object to string"""
        return "{0} {1} {2} {3} {4} {5} {6}"\
            .format(self._from, self._to, self._cc, self._cci,
                    self._subject, self._message)
