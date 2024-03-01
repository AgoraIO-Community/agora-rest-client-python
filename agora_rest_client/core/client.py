import json
import logging
import requests
import sys
import time
from logging.handlers import RotatingFileHandler
from agora_rest_client.core import domain
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
        self._error_code_key = 'error_code'
        self._error_msg_key = 'error_msg'
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

    def build(self):
        """
        Build client
        """
        if self._app_id is None:
            raise exceptions.ClientBuildException('app id is required')

        if self._basic_auth is None:
            raise exceptions.ClientBuildException('basic auth is required')

        # Check region
        if self._domain.get_region() is None:
            raise exceptions.ClientBuildException('region is required')

        if self._domain.get_region() not in domain.RegionArea._value2member_map_:
            raise exceptions.ClientBuildException('region invalid, region:%s' % self._domain.get_region())

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

    def call_api(self, method, url, params=None, post_data=None, post_json=None, headers=None, timeout_seconds=5, response_obj=None):
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

        :type response_obj: object
        :param response_obj: response object

        :return: status_code, response text
        """
        # Retry
        for retry in range(self._http_retry_count):
            retry_num = retry + 1

            try:
                resp = self.do_http_request(method, url, params=params, post_data=post_data, post_json=post_json, headers=headers,
                                                timeout_seconds=timeout_seconds)
                status_code = resp.status_code

                self._logger.debug('call api, url:%s, retry_num:%d, status_code:%d', url, retry_num, status_code)

                # Request success
                if status_code == 200 or status_code == 201:
                    return status_code, resp.text

                # Request failed
                # No need to retry
                if status_code >= 400 and status_code < 410:
                    self._logger.error('call api, status code 400~410 error, err:%s, url:%s, retry_num:%d, status_code:%d, sleep_second:%d', resp.text, url, retry_num, status_code, retry_num)
                    raise exceptions.ClientRequestException(status_code, None, 'status code 400~410 error')

                # Retry
                self._logger.debug('call api, retry, url:%s, retry_num:%d, status_code:%d, sleep_second:%d', url, retry_num, status_code, retry_num)
            except exceptions.ClientRequestException as e:
                self._logger.error('call api, http error, err:%s, url:%s, retry_num:%d', e, url, retry_num)

            # Sleep
            time.sleep(retry_num)

        raise exceptions.ClientRequestException(None, None, 'call api failed')

    def do_http_request(self, method, url, params=None, post_data=None, post_json=None, headers=None, timeout_seconds=5):
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

        :return: class:`requests.Response <Response>` object
        """
        start_time = time.time()

        while True:
            # Retry domain list
            for host in self._domain.get_domain_list():
                host_url = 'https://%s%s' % (host, url)
                self._logger.debug('do http request, host_url:%s', host_url)

                try:
                    resp = requests.request(method, host_url, params=params, data=post_data, json=post_json, headers=headers,
                                            timeout=timeout_seconds, auth=self._basic_auth)

                    self._logger.debug('do http request, host_url:%s, status_code:%d', host_url, resp.status_code)
                    return resp
                except requests.exceptions.RequestException as e:
                    self._logger.error('do http request, request failed, err:%s, host_url:%s, retry:%d', e, host_url)

            # Request timeout
            if time.time() - start_time > self._http_timeout_seconds:
                break

            # Sleep
            time.sleep(0.5)

        raise exceptions.ClientRequestException(None, None, 'do http request failed')

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
