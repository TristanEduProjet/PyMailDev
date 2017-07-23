#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Main window controller"""

# import pickle
import os
import pymaildev
from .controllerQML import ControllerQML


class MainController(ControllerQML):
    """Controller of main.qml"""

    __qml__ = os.path.join(pymaildev.__resources__, "qml", "main.qml")

    def __init__(self, context, parent=None):
        """..."""
        super().__init__(context, parent)

    @staticmethod
    def init_pre_load(context):
        """..."""
        context.setContextProperty("tableModel", ['t1', 't2', 't3'])

    def init_post_load(self):
        """..."""
        self.ctx.setContextProperty("tableModel", ['t4', 't5', 't6'])

# <emails.py>
#     def addEmail(self, person):
#         self._emails.append(person)
#
#     def removeEmail(self, index):
#         return self._emails.pop(index)
#
#     def save(self, filename):
#         output = open(filename, 'w')
#         pickle.dump(self._emails, output)
#
#     def load(self, filename):
#         pkl_file = open(filename, 'r')
#         self._emails = pickle.load(pkl_file)

# <listForm.py>
#     def __replyAction(self):
#         """
#         Reply button event
#         :return:
#         """
#
#         # Load SendForm
#         reply_form = SendForm()
#         reply_form.parent = self
#         self._reply_panel.value = reply_form
#         self._reply_panel.show()
#
#     def __deleteAction(self):
#         """
#         Delete button event
#         :return:
#         """
#         # self._emails.__sub__(0)
#
#     def __optionsAction(self):
#         """
#         Options button event
#         :return:
#         """
#         # Load ParametersForm
#         param_form = ParametersForm()
#         param_form.parent = self
#         self._param_panel.value = param_form
#         self._param_panel.show()
#
#     def __load_emails(self):
#         """
#         Load all Email objects et insert them into the ControlList
#         :return:
#         """
