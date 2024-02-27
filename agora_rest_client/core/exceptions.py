class ClientException(Exception):
    def __init__(self, status_code, error_code, error_msg):
        """
        The base exception class.
        """
        super(ClientException, self).__init__()

        # Http status code
        self.status_code = status_code
        # Error code
        self.error_code = error_code
        # Error message
        self.error_msg = error_msg

    def __str__(self):
        return "%s - {status_code:[%s],error_code:[%s],error_msg:[%s] }" % (self.__class__.__name__, self.status_code, self.error_code, self.error_msg)

class ServiceResponseException(ClientException):
    def __init__(self, status_code, error_code, error_msg):
        """
        The base exception class of service response exceptions.
        """
        super(ServiceResponseException, self).__init__(status_code, error_code, error_msg)

    def __str__(self):
        return "%s - {status_code:[%s],error_code:[%s],error_msg:[%s] }" % (self.__class__.__name__, self.status_code, self.error_code, self.error_msg)

class ClientBuildException(ClientException):
    def __init__(self, error_msg):
        """
        Client Build Exception
        """
        super(ClientBuildException, self).__init__(None, None, error_msg)

class ClientRequestException(ServiceResponseException):
    def __init__(self, status_code, error_code, error_msg):
        """
        Client Request Exception
        """
        super(ClientRequestException, self).__init__(status_code, error_code, error_msg)
