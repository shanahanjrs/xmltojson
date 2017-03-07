#!/usr/bin/env python

"""
xmltojson
John Shanahan

Simple cli xml to json converter using the xmltodict library
"""

import sys
import os
import xmltodict
import json

version = '0.1'

def _usage():
    print('xmltojson {version}'.format(version=version))
    print('Usage: xmltojson [options] <example.xml>')
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


def _xml_string_to_json(xml_string):
    """ _xml_string_to_json
    Takes an xml string and returns the json equivalent
    """

    return json.dumps(xmltodict.parse(xml_string))


def _tr_xml_to_json_extension(xml_filename):
    """ _tr_xml_to_json_extension
    Translates asdf.xml to asdf.json (just the filename)
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


def main(xml_filename):
    """ Main
    Takes a filename and reads the xml contents of it and creates a json file
    """

    if '-v' in sys.argv or '--version' in sys.argv:
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
    json_obj = _xml_string_to_json(xml_string)

    # Create json output file
    if "--file" in sys.argv:
        _write_output_file(json_filename, json_obj)
    else:
        print(json_obj)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print('xml filename required...')
        sys.exit(1)