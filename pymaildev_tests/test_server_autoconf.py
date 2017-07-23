#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test fonctionnement auto-conf du serveur"""

import unittest
from pymaildev.core.server import ServerAutoConf


class AutoConfServerTest(unittest.TestCase):
    """..."""

    def test_load_yml(self):
        """..."""
        tmp = ServerAutoConf().all_confs
        self.assertIsNotNone(tmp)
        self.assertTrue(tmp)  # not(tmp)

    def test_from_registed_adresse(self):
        """..."""
        self.assertIsNotNone(ServerAutoConf().get_conf("mon-mail@free.fr"))

    def test_from_unregisted_adresse(self):
        """..."""
        self.assertIsNone(ServerAutoConf().get_conf("mon-mail@not-exist.fr"))
