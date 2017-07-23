#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Mail window' composer controller"""

import os
import pymaildev
from .controllerQML import ControllerQML


class MailController(ControllerQML):
    """Controller of mail.qml"""

    __qml__ = os.path.join(pymaildev.__resources__, "qml", "mail.qml")

    def __init__(self, context, parent=None):
        """..."""
        super().__init__(context, parent)

# <sendFrom.py>
#     def __sendAction(self):
#         """
#         Send button event
#         :return:
#         """
#         # Retrieve the form' ControlText values to compose the Email to send
#         try:
#             message = emails.html(html=self._message.value, subject=self._subject.value,
#                                   mail_from=(self._fullname.value, self._from.value))
#         except Exception:
#             self._logs.value += "Error: Incorrect entered values.\n"
#             raise
#
#         # Send the message with the parameters formerly defined
#         try:
#             response = message.send(to=self._to.value,
#                                     smtp={"host": "smtp.gmail.com", "port": 465, "ssl": True,
#                                           "user": "A CHANGER", "password": "A CHANGER"})
#         except Exception:
#             self._logs.value += "Error: Incorrect SMTP configuration.\n"
#             raise
#
#         # Assert the email has been correctly sent and received by the recipient
#         assert response.status_code == 250
#
#         if response.status_code == 250:
#             self._logs.value += "Email sent to " + self._to.value + ".\n"
#             # TODO: Stocker l'email envoyé dans une autre liste graphique ?
#
#     def __clearAction(self):
#         """
#         Clear button event. Reset the textarea '_message' value.
#         :return:
#         """
#         self._message.value = ''
