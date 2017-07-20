#!/bin/python
# -*-coding:utf-8 -*

"""
Main PyMailDev

Point d'entrée si appelé comme module, ou comme programme.
"""

import sys
# from . import gui
from .gui import start_qml
from .gui import MainController
# from __init__ import *
# from . import *


def main(args=None):
    """Main routine."""
    if args is None:
        args = sys.argv[1:]
    start_qml(args, MainController)


if __name__ == "__main__":
    main(sys.argv)
