# xmltojson
Cli tool to convert XML to JSON

## To install

### Pypi:
`$ pip install xmltojson`

## To use

### Command line:
`$ xmltojson.py <filename.xml>`

### Py module:
```
>>> import xmltojson
>>> my_xml = '<test><name>John Shanahan</name></test>'
>>> xmltojson.parse(my_xml)
'{"test": {"name": "John Shanahan"}}'
```
