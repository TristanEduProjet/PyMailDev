#!/bin/python
# -*-coding:utf-8 -*

"""
Main PyMailDev

Entry point if called as a module or a program.
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
