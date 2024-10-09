from ._parser import HTTPRequest

def parse(raw_request: str) -> HTTPRequest:
    """
    Parse a raw HTTP request string into an HTTPRequest object.
    
    Args:
        raw_request (str): Raw HTTP request string
    
    Returns:
        HTTPRequest: Parsed HTTP request object
    
    Example:
        >>> import http_parser
        >>> request = http_parser.parse(raw_http_string)
        >>> print(request.headers)
        >>> print(request.body)
    """
    return HTTPRequest(raw_request)

__all__ = ['parse', 'HTTPRequest']
__version__ = "0.1.4"