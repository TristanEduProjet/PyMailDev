#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject, pyqtProperty

class EmailResume(QObject):
    """Email simple/partial model"""

    def __init__(self, parent=None):
        super().__init__(parent)

    @pyqtProperty('QString')
    @property
    def of(self):
        return self._from

    @of.setter
    def of(self, of):
        self._from = of

    @pyqtProperty('QString')
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject):
        self._subject = subject

    # TODO : date reçu

    @staticmethod
    def create(ffrom, subject, message, parent=None):
        """Create object mail from existing data"""
        mail = EmailResume(parent)
        mail.of(ffrom)
        mail.subject(subject)

    def __str__(self):
        """Object to string"""
        return "{0} {1}"\
            .format(self._from, self._subject)
