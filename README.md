# HTTP Parse

A lightweight Python library for parsing raw HTTP requests.

## Installation

```bash
pip install http-parse
```

## Usage

```python
from http_parse import parse

raw_request = """
GET /path HTTP/1.1
Host: example.com
User-Agent: curl/8.5.0

{"data": "example"}
"""

parsed = parse(raw_request)
print(parsed.headers)  # Access headers (dictionary format)
print(parsed.body)     # Access body 
print(parsed.path)      # Access requested path (/foo/bar)
```

## Features

- Parse HTTP headers into a dictionary
- Access request body
- Access and modify headers
- Extract URL and HTTP method

## License

MIT License