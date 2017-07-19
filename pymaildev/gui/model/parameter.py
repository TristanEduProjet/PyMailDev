#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Parameter(object):
    """Parameter model"""

    def __init__(self, host, port, ssl, user, password):
        self._host = host
        self._port = port
        self._ssl = ssl
        self._user = user
        self._password = password

    def _get_host(self):
        return self._host

    def _get_port(self):
        return self._port

    def _get_ssl(self):
        return self._ssl

    def _get_user(self):
        return self._user

    def _get_password(self):
        return self._password

    def _set_host(self, host):
        self._host = host

    def _set_port(self, port):
        self._port = port

    def _set_ssl(self, ssl):
        self._ssl = ssl

    def _set_user(self, user):
        self._user = user

    def _set_password(self, password):
        self._password = password

    host = property(_get_host, _set_host)
    port = property(_get_port, _set_port)
    ssl = property(_get_ssl, _set_ssl)
    user = property(_get_user, _set_user)
    password = property(_get_password, _set_password)
