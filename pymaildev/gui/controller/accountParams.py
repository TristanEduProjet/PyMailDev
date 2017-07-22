#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Main window controller"""

# import pickle
# import json
# import io
import os
import pymaildev
from .controllerQML import ControllerQML


class AccountParamsController(ControllerQML):
    """Controller of accountParams.qml"""

    __qml__ = os.path.join(pymaildev.__resources__, "qml", "accountParams.qml")

    def __init__(self, context, parent=None):
        """..."""
        super().__init__(context, parent)

# <parameters.py>
#     def save_parameters(self, host, port, ssl, user, password):
#         # Create the file or append at the end-of-file
#         self._params = {"host": host,
#                         "port": port,
#                         "ssl": ssl,
#                         "user": user,
#                         "password": password}
#         pickle.dump(self._params, open("PyMailDev/resources/parameters.ini", "wb"))
#
#     def load_parameters(self):
#         # Get parameters from parameters.ini
#         self._params = pickle.load(open("PyMailDev/resources/parameters.ini", "rb"))

# <parametersForm.py>
#     def __saveParamsAction(self):
#         """
#         Save button event
#         :return:
#         """
#         try:
#             self.__save_parameters()
#         except IOError:
#             raise
#
#     def __loadParamsAction(self):
#         """
#         Load button event
#         :return:
#         """
#         try:
#             self.__load_parameters()
#         except IOError:
#             raise
#
#     def __save_parameters(self):
#         """
#         Save function : Save the entered parameters into the JSON file by replacing the old ones.
#         If the file doesn't exist, it is still created.
#         :return:
#         """
#         # Encrypt password and store the data into a dictionary
#         self._password.value = Encryption.encode("SecretMessageOfTheDead", self._password.value)
#         self.dict_params = {"host": self._host.value,
#                             "port": self._port.value,
#                             "ssl": self._ssl.value,
#                             "user": self._user.value,
#                             "password": self._password.value}
#         # Write JSON file
#
#         with io.open("C:\\Users\\Olivier\\PycharmProjects\\PyMailDev\\pymaildev\\resources\\parameters.json", 'w',
#                      encoding='utf8') as outfile:
#             str_ = json.dumps(self.dict_params, indent=4, sort_keys=True, separators=(',', ': '),
#                               ensure_ascii=False)
#             outfile.write(str_)
#
#     def __load_parameters(self):
#         """
#         Load function : Load the saved parameters from the JSON file and stores them
#         :return:
#         """
#         # Read JSON file
#         with open("C:\\Users\\Olivier\\PycharmProjects\\PyMailDev\\pymaildev\\resources\\parameters.json") as data_file:
#             self.dict_params.update(json.load(data_file))
#         # Update controls values
#         self._host.value = self.dict_params['host']
#         self._port.value = self.dict_params['port']
#         self._ssl.value = self.dict_params['ssl']
#         self._user.value = self.dict_params['user']
#         self._password.value = self.dict_params['password']
