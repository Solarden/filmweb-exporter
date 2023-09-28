class BasicException(Exception):
    """Basic Exception with self message, and status code"""

    def __init__(self, message, code=None):
        self.message = message
        self.code = code

    def __str__(self):
        return self.message
