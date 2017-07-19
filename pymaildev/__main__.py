#!/bin/python
# -*-coding:utf-8 -*

"""Point d'entrée si appelé comme module, ou comme programme."""

import sys
import pyforms
from gui import ListForm
# from __init__ import *
# from . import *


def main(args=None):
    """Main routine."""
    if args is None:
        args = sys.argv[1:]
    pyforms.start_app(ListForm, geometry=(810, 540, 800, 400))


if __name__ == "__main__":
    main()
