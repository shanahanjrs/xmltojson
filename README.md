# xmltojson

---

Python library and cli tool for converting XML to JSON

[![Downloads](https://static.pepy.tech/personalized-badge/xmltojson?period=total&units=international_system&left_color=lightgrey&right_color=brightgreen&left_text=Installs)](https://pepy.tech/project/xmltojson)

## Install

`$ poetry add xmltojson`

`$ pip install xmltojson`

## Usage

### Command line:

#### Converting an XML file and sending the output to STDOUT
`$ xmltojson <filename.xml>`

#### Send output to a file
`$ xmltojson <filename.xml> -o <new_filename.json>`

#### xmltojson can also read from STDIN
`$ echo '<name>John</name>' | xmltojson --stdin`

### Library:
```
[1]: import xmltojson
[2]: with open('/path/to/file', 'r') as f:
...:     my_xml = f.read()
[3]: xmltojson.parse(my_xml)
'{"name": "John"}'
```
