#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject, pyqtProperty


class Account(QObject):
    """Parameter model"""

    def __init__(self, host, port, ssl, user, password, parent=None):
        super().__init__(parent)
        self.host = host
        self.port = port
        self.ssl = ssl
        self.user = user
        self.password = password

    @property
    @pyqtProperty('QString')
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    @pyqtProperty('QString')
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    @pyqtProperty('QString')
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


    @property
    @pyqtProperty('QString')
    def receive_host(self):
        return self._host

    @receive_host.setter
    def receive_host(self, host):
        self._host = host

    @property
    @pyqtProperty(int)
    def receive_port(self):
        return self._port

    @receive_port.setter
    def receive_port(self, port):
        self._port = port

    @property
    @pyqtProperty(int)
    def receive_ssl(self):
        return self._ssl

    @receive_ssl.setter
    def receive_ssl(self, ssl):
        self._ssl = ssl


    @property
    @pyqtProperty('QString')
    def send_host(self):
        return self._host

    @send_host.setter
    def send_host(self, host):
        self._host = host

    @property
    @pyqtProperty(int)
    def send_port(self):
        return self._port

    @send_port.setter
    def send_port(self, port):
        self._port = port

    @property
    @pyqtProperty(int)
    def send_ssl(self):
        return self._ssl

    @send_ssl.setter
    def send_ssl(self, ssl):
        self._ssl = ssl
