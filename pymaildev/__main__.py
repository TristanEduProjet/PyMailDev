#!/bin/python
# -*-coding:utf-8 -*

"""Point d'entrée si appelé comme module, ou comme programme."""

import sys
# from __init__ import *
# from . import *


def main(args=None):
    """Main routine."""
    if args is None:
        args = sys.argv[1:]
    print("main called")


if __name__ == "__main__":
    print("Hello world !")
    # main()
