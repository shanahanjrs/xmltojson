"""
Simple command line tool to convert xml into json using xmltodict

cli.py
John Shanahan
Usage:
    cli.py.py <example.xml> [options]
Options:
   --version -v              Version number
   --file                    Output to file instead of STDOUT
"""

import json
import xmltodict # type: ignore


__version__ = '2.0.3'  # must match pyproject.toml


def _usage() -> None:
    print(f'xmltojson {__version__}')
    print('author: John Shanahan <shanahan.jrs@gmail.com>\n')
    print('Usage:')
    print('    $ cli.py <example.xml> [options]')
    print('    $ echo "<name>John</name>" | cli.py --stdin [options]')
    print()
    print('Options:')
    print('    --version -v              Version number')
    print('    -o                        Output to file instead of STDOUT\n')


def _read_xml_file(filename: str) -> str:
    """
    Takes a filename and reads it and returns the contents
    """
    with open(filename, 'r') as file_obj:
        ret = file_obj.read()
        file_obj.close()

    return ret


def _tr_xml_to_json_extension(xml_filename: str) -> str:
    """
    Translates example.xml to example.json (just the filename)
    """
    if '.xml' in xml_filename:
        return xml_filename.replace('.xml', '.json')
    else:
        return xml_filename + '.json'


def _write_output_file(json_filename: str, json_contents: str) -> None:
    """
    Just writes text to a file.
    """
    with open(json_filename, 'w') as file_obj:
        file_obj.write(json_contents)
        file_obj.close()


def _lists_share_element(list_a: list, list_b: list) -> bool:
    """
    Check if list_a shares and element with list_b
    """
    return not set(list_a).isdisjoint(list_b)


def parse(xml_string: str) -> str:
    """
    Takes an xml string and returns the json equivalent
    """
    return json.dumps(xmltodict.parse(xml_string))
