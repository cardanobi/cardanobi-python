
from functools import wraps
from urllib.parse import urlencode

class APIResponseException(Exception):
    def __init__(self, status, message=""):
        super().__init__(f"HTTP request failed with status {status}: {message}")
        self.status = status
        self.message = message

def handleError(error, response):
    print(f"CardanoBI - handleError, status: {response.status}, error: {error}")
    return {"status": response.status, "error": error};

class ApiError(Exception):
    """Custom API error to handle HTTP errors."""
    def __init__(self, response):
        self.response = response
        super().__init__(f"CardanoBI - request failed with status {response.status}")

def get_query_params(options, allowed_params):
    """
    Constructs a query string from the options dictionary, including only keys that are in allowed_params,
    and handles 'query' parameter specially.
    
    :param options: Dictionary of all provided options.
    :param allowed_params: List of keys that are allowed to be included in the query string.
    :return: A query string to be appended to the endpoint URL.
    """
    # Extract and remove 'query' from options if it exists
    query_value = options.pop('query', None)
    
    # Filter options to include only keys that are allowed and have non-None values
    filtered_options = {key: value for key, value in options.items() if key in allowed_params and value is not None}
    
    # Use urlencode to construct the query string with proper encoding for the allowed_params
    query_string = urlencode(filtered_options)
    
    # If 'query' was present, append its value directly to the query string without its name
    if query_value is not None:
        # Check if there are already other parameters in the query string to append correctly
        if query_string:
            query_string += "&" + query_value  # Append with '&' if other params exist
        else:
            query_string = query_value  # Use directly if no other params
    
    return query_string

