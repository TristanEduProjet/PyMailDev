#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module configuration serveur mail

Utils pour la configuration du serveur de mail
"""

import pymaildev
import yaml
import os
from .types import *
import pprint


class ServerAutoConf:
    """..."""

    def __init__(self):
        """..."""
        with open(os.path.join(pymaildev.__resources__, "mails_param.yml"), 'r') as f:
            self._doc = self.parse_yml(yaml.load(f))
            f.close()
        # load(...) / load_all(...)

    def get_conf(self, adrmail):
        """..."""
        domain = adrmail.split('@', )[-1]  # num=len(adrmail)
        try:
            return self._doc[domain]
        except:
            return None

    @property
    def all_confs(self):
        """..."""
        return self._doc

    @staticmethod
    def parse_yml(doc_yml):
        """..."""
        alls = {}
        for k, v in doc_yml.items():
            tmp = ServerConf(v)
            for d in tmp._adrss:
                alls[d] = tmp
        return alls


class ServerConf:
    """Bean config server"""

    def __init__(self, obj_yml=None):
        """..."""
        if obj_yml is not None:
            self._adrss = obj_yml['adresse']
            params = obj_yml['params']
            pin = params['in'][params['prefer']['in']]
            self._receive = {'host': pin['host'],
                             'port': pin['port'],
                             'type': TypeReceive[pin['type'].upper()],
                             'security': TypeSecurity(pin['protocol'])}
            pout = params['out'][params['prefer']['out']]
            self._receive = {'host': pout['host'],
                             'port': pout['port'],
                             'type': TypeReceive[pin['type'].upper()],
                             'security': TypeSecurity(pin['protocol'])}

    # getters & setters

    # def __str__(self):
    #     return "".format()
