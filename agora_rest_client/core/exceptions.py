class ClientException(Exception):
    """
    Client exceptions
    """

    def __init__(self, status_code, error_code, error_msg):
        super(ClientException, self).__init__()

        # Http status code
        self.status_code = status_code
        # Error code
        self.error_code = error_code
        # Error message
        self.error_msg = error_msg

    def __str__(self):
        return "%s - {status_code:[%s],error_code:[%s],error_msg:[%s]}" % (self.__class__.__name__, self.status_code, self.error_code, self.error_msg)

class AttributeException(ClientException):
    """
    Attribute exceptions
    """

    def __init__(self, error_msg):
        super(AttributeException, self).__init__(None, None, error_msg)

class ServiceResponseException(ClientException):
    """
    Service response exceptions
    """

    pass

class ClientBuildException(ClientException):
    """
    Client Build Exception
    """

    def __init__(self, error_msg):
        super(ClientBuildException, self).__init__(None, None, error_msg)

class ClientRequestException(ServiceResponseException):
    """
    Client Request Exception
    """

    pass

class ClientTimeoutException(ClientRequestException):
    """
    Client Timeout Exception
    """

    pass
