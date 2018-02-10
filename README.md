# xmltojson
Cli tool to convert XML to JSON

## To install

### Pypi:
`$ pip install xmltojson`

## Usage

### Command line:

#### Converting an XML file and returning the output to STDOUT
`$ xmltojson <filename.xml>`

#### Send output to a file
`$ xmltojson <filename.xml> -o <new_filename.json>`

#### xmltojson can also read from STDIN
`$ echo '<name>John</name>' | xmltojson --stdin`

### Py module:
```
[1]: import xmltojson
[2]: with open('/path/to/file', 'r') as f:
...:     my_xml = f.read()
[3]: xmltojson.parse(my_xml)
'{"name": "John"}'
```
