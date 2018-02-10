#!/usr/bin/env python3

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

import json
import os
import sys
import xmltodict

import utils

# --- Def

def _usage():
    print('xmltojson {version}'.format(version=utils.__version__))
    print('shanahan.jrs@gmail.com')
    print()
    print('Usage:')
    print('    $ xmltojson <example.xml> [options]')
    print('    $ echo "<name>John</name>" | xmltojson --stdin [options]')
    print()
    print('Options:')
    print('    --version -v              Version number')
    print('    -o                        Output to file instead of STDOUT')
    print()


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

