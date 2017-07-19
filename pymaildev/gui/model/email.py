#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Email(object):
    """Email Model"""

    def __init__(self, fullname, ffrom, to, cc, cci, subject, message):
        self._fullname      = fullname
        self._from          = ffrom
        self._to            = to
        self._cc            = cc
        self._cci           = cci
        self._subject       = subject
        self._message       = message

    def __str__(self):
        """Object to string"""
        return "{0} {1} {2} {3} {4} {5} {6}"\
            .format(self._fullname, self._from, self._to, self._cc,
                    self._cci, self._subject, self._message)
