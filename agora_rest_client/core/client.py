import func_timeout
import logging
import requests
import sys
import time
from logging.handlers import RotatingFileHandler
from agora_rest_client.core import domain
from agora_rest_client.core import errors
from agora_rest_client.core import exceptions
from agora_rest_client.core import log

class Client(object):
    """
    Base client
    """

    def __init__(self):
        self._app_id = None
        self._basic_auth = None
        self._domain = domain.default_domain
        self._file_logger_handler = None
        self._http_retry_count = 3
        self._http_timeout_seconds = 10
        self._logger = self._init_logger()
        self._stream_logger_handler = None

    @classmethod
    def _init_logger(cls):
        """
        Init logger
        """
        logger_name = '%s-%s-%d' % (log.LOGGER_NAME, cls.__name__, time.time()*1000000)
        logger = logging.getLogger(logger_name)
        logger.propagate = False

        return logger

    def new_builder():
        return Client()

    def build(self):
        """
        Build client
        """
        if self._app_id is None:
            raise exceptions.ClientBuildException(errors.APP_ID_REQUIRED)

        if self._basic_auth is None:
            raise exceptions.ClientBuildException(errors.BASIC_AUTH_REQUIRED)

        # Check region
        if self._domain.get_region() is None:
            raise exceptions.ClientBuildException(errors.REGION_REQUIRED)

        if self._domain.get_region() not in domain.RegionArea._value2member_map_:
            raise exceptions.ClientBuildException(errors.REGION_INVALID)

        if self._file_logger_handler is not None:
            self.add_file_logger(**self._file_logger_handler)
        if self._stream_logger_handler is not None:
            self.add_stream_logger(**self._stream_logger_handler)

        self._domain.run(self._logger)

        return self

    def add_file_logger(self, path, log_level, max_bytes, backup_count, format_string):
        """
        Add file logger

        :type path: str
        :param path: log file path

        :type log_level: int
        :param log_level: log level

        :type max_bytes: int
        :param max_bytes: max bytes

        :type backup_count: int
        :param backup_count: backup count

        :type format_string: str
        :param format_string: format string
        """
        self._logger.setLevel(log_level)
        file_handler = RotatingFileHandler(path, maxBytes=max_bytes, backupCount=backup_count)
        file_handler.setLevel(log_level)
        formatter = logging.Formatter(format_string if format_string is not None else log.LOGGER_FORMAT)
        file_handler.setFormatter(formatter)

        if file_handler not in self._logger.handlers:
            self._logger.addHandler(file_handler)

    def add_stream_logger(self, stream, log_level, format_string):
        """
        Add stream logger

        :type stream: object
        :param stream: stream

        :type log_level: int
        :param log_level: log level

        :type format_string: str
        :param format_string: format string
        """
        self._logger.setLevel(log_level)
        stream_handler = logging.StreamHandler(stream)
        stream_handler.setLevel(log_level)
        formatter = logging.Formatter(format_string if format_string is not None else log.LOGGER_FORMAT)
        stream_handler.setFormatter(formatter)

        if stream_handler not in self._logger.handlers:
            self._logger.addHandler(stream_handler)

    @property
    def app_id(self):
        return self._app_id

    def call_api(self, method, url, params=None, post_data=None, post_json=None, headers=None, timeout_seconds=5, trace_id=None):
        """
        Call api

        :type method: str
        :param method: http method

        :type url: str
        :param url: http url

        :type params: object
        :param params: http params

        :type post_data: object
        :param post_data: http post data

        :type post_json: object
        :param post_json: http post json

        :type headers: object
        :param headers: http headers

        :type timeout_seconds: int
        :param timeout_seconds: http timeout

        :type trace_id: string
        :param trace_id: trace id

        :type: object
        :return: class:`requests.Response <Response>` object
        """
        try:
            resp = func_timeout.func_timeout(self._http_timeout_seconds, self.do_http_request, args=(method, url),
                                             kwargs={'params': params, 'post_data': post_data, 'post_json': post_json, 'headers': headers,
                                                     'timeout_seconds': timeout_seconds, 'trace_id': trace_id})
            return resp
        except func_timeout.FunctionTimedOut as e:
            raise exceptions.ClientTimeoutException(None, None, e.getMsg())
        except Exception as e:
            raise exceptions.ClientRequestException(None, None, str(e))

    def do_http_request(self, method, url, params=None, post_data=None, post_json=None, headers=None, timeout_seconds=5, trace_id=None):
        """
        Request http

        :type method: str
        :param method: http method

        :type url: str
        :param url: http url

        :type params: object
        :param params: http params

        :type post_data: object
        :param post_data: http post data

        :type post_json: object
        :param post_json: http post json

        :type headers: object
        :param headers: http headers

        :type timeout_seconds: int
        :param timeout_seconds: http timeout

        :type trace_id: string
        :param trace_id: trace id

        :type: object
        :return: class:`requests.Response <Response>` object
        """
        status_code = None

        while True:
            for host in self._domain.get_domain_list():
                host_url = 'https://%s%s' % (host, url)
                self._logger.debug('do http request, trace_id:%s, host_url:%s', trace_id, host_url)

                try:
                    resp = requests.request(method, host_url, params=params, data=post_data, json=post_json, headers=headers,
                                            timeout=timeout_seconds, auth=self._basic_auth)
                    status_code = resp.status_code

                    self._logger.debug('do http request, trace_id:%s, host_url:%s, status_code:%s', trace_id, host_url, status_code)
                    return resp
                except requests.exceptions.RequestException as e:
                    self._logger.error('do http request, request failed, err:%s, trace_id:%s, host_url:%s, status_code:%s', e, trace_id, host_url, status_code)

                # Sleep
                time.sleep(0.5)

    @property
    def logger(self):
        return self._logger

    def with_app_id(self, app_id):
        self._app_id = app_id

        return self

    def with_basic_auth(self, user_name, password):
        self._basic_auth = (user_name, password)

        return self

    def with_http_retry_count(self, _http_retry_count):
        self._http_retry_count = _http_retry_count

        return self

    def with_http_timeout_seconds(self, http_timeout_seconds):
        self._http_timeout_seconds = http_timeout_seconds

        return self

    def with_file_log(self, path, log_level=logging.INFO, max_bytes=10 * 1024 * 1024, backup_count=2, format_string=None):
        self._file_logger_handler = {
            "backup_count": backup_count,
            "format_string": format_string,
            "log_level": log_level,
            "max_bytes": max_bytes,
            "path": path
        }

        return self

    def with_region(self, region):
        self._domain.set_region(region)

        return self

    def with_stream_log(self, stream=sys.stdout, log_level=logging.INFO, format_string=None):
        self._stream_logger_handler = {
            "format_string": format_string,
            "log_level": log_level,
            "stream": stream
        }

        return self
