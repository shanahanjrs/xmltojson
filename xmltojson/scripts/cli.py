#!/usr/bin/env python3

import sys
import os

import xmltojson
import utils


def _get_input() -> str:

    # STDIN support
    if '--stdin' in sys.argv:
        # Get input from stdin
        with sys.stdin as f:
            xml_str = f.read()

    # file input
    else: 
        with open(os.getcwd() + '/' + sys.argv[1], 'r') as f:
            xml_str = f.read()

    return xml_str


def _get_input_filename() -> str:
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'out.xml'

    return filename


def main() -> None:

    if len(sys.argv) < 2:
        xmltojson._usage()
        sys.exit(1)

    # version num output
    if '-v' in sys.argv or '--version' in sys.argv:
        print(utils.__version__)
        sys.exit(0)

    xml_str = _get_input()
    json_obj = xmltojson.parse(xml_str)

    # Create json output file
    if '-o' in sys.argv:
        json_filename = sys.argv[sys.argv.index('-o')+1]
        xmltojson._write_output_file(json_filename, json_obj)
    else:
        print(json_obj)


if __name__ == "__main__":
    main()
