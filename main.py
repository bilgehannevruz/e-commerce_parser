#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import logging




from src.interface import Interface

def main(args: argparse.Namespace):
    """ Main entry point of the app """
    try:
        interface = Interface()
        sitemap = interface.create_sitemap(address=args.input)
        parser = interface.create_parser(sitemap=sitemap)
        interface.run(sitemap=sitemap, parser=parser)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser(description="Provided address being parsed for each product and stored in database")
    parser.add_argument("-i", "--input", type=str, help="Address to be parsed", required=True)
    args = parser.parse_args()
    main(args)