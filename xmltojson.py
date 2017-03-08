#!/usr/bin/env python


"""
Simple command line tool to convert xml into json using xmltodict
"""

# xmltojson
# John Shanahan
# Usage:
#     xmltojson.py <example.xml> [options]
# Options:
#    --version -v              Version number
#    --file                    Output to file instead of STDOUT


# --- Setup

import sys
import os
import xmltodict
import json

__author__ = 'John Shanahan'
__version__ = '0.1.1'
__license__ = 'Apache'


# --- Def

def _usage():
    print('xmltojson {version}'.format(version=__version__))
    print('Usage: xmltojson.py <example.xml> [options]')
    print('Options:')
    print('    --version -v              Version number')
    print('    --file                    Output to file instead of STDOUT')


def _read_xml_file(filename):
    """ _read_xml_file
    Takes a filename and reads it and returns the contents
    """

    with open(filename, 'r') as file_obj:
        ret = file_obj.read()
        file_obj.close()

    return ret


def _tr_xml_to_json_extension(xml_filename):
    """ _tr_xml_to_json_extension
    Translates example.xml to example.json (just the filename)
    """

    if '.xml' in xml_filename:
        return xml_filename.replace('.xml', '.json')
    else:
        return xml_filename + '.json'


def _write_output_file(json_filename, json_contents):
    """ _write_output_file
    Just writes text to a file.
    """

    with open(json_filename, 'w') as file_obj:
        file_obj.write(json_contents)
        file_obj.close()


def _lists_share_element(list_a, list_b):
    """ _lists_share_element
    Check if list_a shares and element with list_b
    """
    return not set(list_a).isdisjoint(list_b)


def parse(xml_string):
    """ parse
    Takes an xml string and returns the json equivalent
    """
    return json.dumps(xmltodict.parse(xml_string))


if __name__ == "__main__":

    if len(sys.argv) > 1:

        xml_filename = sys.argv[1]

        option_version = ['v', '-v', '--v', 'version', '-version', '--version']
        option_file = ['f', '-f', '--f', 'file', '-file', '--file']

        if _lists_share_element(sys.argv, option_version):
            _usage()
            sys.exit()

        if not os.path.exists(xml_filename):
            print('File not found...')
            sys.exit(1)

        # Create filename for json output file
        json_filename = _tr_xml_to_json_extension(xml_filename)

        # Grab xml from file
        xml_string = _read_xml_file(xml_filename)

        # Translate xml to json from the string we got
        json_obj = parse(xml_string)

        # Create json output file
        if _lists_share_element(sys.argv, option_file):
            _write_output_file(json_filename, json_obj)
        else:
            print(json_obj)

    else:
        print('xml filename required...')
        sys.exit(1)