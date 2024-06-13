# Description

My stupid python json parser.

**It has no validation and no error reports!!!** (at least yet)

# Details

The `Parser` class provides `parse_file()` method that accept one str parameter - path to json file. `parse_file()` method returns python dictionary representation of json file content.

# Usagde

```python

parser = Parser()
data = parser.parse_file("path/to/file.json")
print(data)

```
