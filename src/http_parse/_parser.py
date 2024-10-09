class HTTPRequest:
    """
    A class representing an HTTP request.
    
    Attributes:
        headers (dict): Dictionary of HTTP headers
        body (str): Request body
        method (str): HTTP method (GET, POST, etc.)
        path (str): Requested path
        http_version (str): HTTP version
    """
    
    def __init__(self, raw_request: str):
        """
        Initialize an HTTPRequest object.
        
        Args:
            raw_request (str): Raw HTTP request string
        """
        self.raw_request = raw_request.strip()
        self.headers = {}
        self.body = ""
        self.method = ""
        self.path = ""
        self.http_version = ""
        self._parse()
    
    def _parse(self):
        """Parse the raw HTTP request into its components."""
        # Split the request into headers and body
        parts = self.raw_request.split('\n\n', 1)
        headers_section = parts[0]
        self.body = parts[1] if len(parts) > 1 else ""
        
        # Split headers into lines
        header_lines = headers_section.split('\n')
        
        # Parse the request line (first line)
        if header_lines:
            request_line = header_lines[0].split(' ')
            if len(request_line) >= 3:
                self.method = request_line[0]
                self.path = request_line[1]
                self.http_version = request_line[2]
        
        # Parse the headers
        for line in header_lines[1:]:
            if ':' in line:
                key, value = line.split(':', 1)
                self.headers[key.strip()] = value.strip()

    def __repr__(self):
        return f"HTTPRequest(method='{self.method}', path='{self.path}', headers={len(self.headers)} items)"