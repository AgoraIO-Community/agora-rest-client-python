import json
import logging
import requests
import sys
import time
from logging.handlers import RotatingFileHandler
from agora_rest_client.core import domain
from agora_rest_client.core import exceptions
from agora_rest_client.core import log
from agora_rest_client.core import response

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
        self._logger = self._init_logger()
        self._retry_count = 3
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

        :param path: log file path
        :param log_level: log level
        :param max_bytes: max bytes
        :param backup_count: backup count
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

        :param stream: stream
        :param log_level: log level
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
    
    def call_api(self, method, url, params=None, post_data=None, post_json=None, headers=None, timeout_seconds=5, 
                 response_type=response.ResponseType.OBJECT.value, response_obj=None):
        """
        Call api

        :param method: http method
        :param url: http url
        :param params: http params
        :param post_data: http post data
        :param post_json: http post json
        :param headers: http headers
        :param timeout_seconds: http timeout
        :param response_type: response type
        :param response_obj: response object
        :return: response
        """
        return self.do_http_request(method, url, params, post_data, post_json, headers, timeout_seconds, response_type, response_obj)

    def do_http_request(self, method, url, params=None, post_data=None, post_json=None, headers=None, timeout_seconds=5, 
                        response_type=response.ResponseType.OBJECT.value, response_obj=None):
        """
        Request http
        
        :param method: http method
        :param url: http url
        :param params: http params
        :param post_data: http post data
        :param post_json: http post json
        :param headers: http headers
        :param timeout_seconds: http timeout
        :param response_type: response type, `agora_rest_client.core.response.ResponseType`
        :param response_obj: response object
        :return: response
        """
        status_code = None
        error_code = None
        error_msg = None

        # Retry domain list
        for item in self._domain.get_domain_list():
            for retry in range(self._retry_count):
                retry_num = retry + 1
                host_url = 'https://%s%s' % (item['host'], url)
                self._logger.debug('do http request, host_url:%s, retry:%d', host_url, retry_num)

                try:
                    resp = requests.request(method, host_url, params=params, data=post_data, json=post_json, headers=headers, 
                                                timeout=timeout_seconds, auth=self._basic_auth)
                    status_code = resp.status_code

                    self._logger.debug('do http request, host_url:%s, retry:%d, status_code:%d', host_url, retry_num, status_code)

                    # Request success
                    if status_code == 200:
                        if response_type == response.ResponseType.JSON.value:
                            return resp.json()
                        elif response_type == response.ResponseType.OBJECT.value:
                            return json.loads(resp.text, object_hook=response_obj)
                        elif response_type == response.ResponseType.TEXT.value:
                            return resp.text

                        return resp.text

                    resp_json = resp.json()
                    error_code = resp_json.get(self._error_code_key)
                    error_msg = resp_json.get(self._error_msg_key) if resp_json.get(self._error_msg_key) is not None else resp.text

                    # Request failed
                    # No need to retry
                    if status_code > 200 and status_code <= 300:
                        self._logger.error('do http request, status code 200~300 error, err:%s, host_url:%s, retry:%d, status_code:%d, sleep_second:%d', resp.text, host_url, retry_num, status_code, retry_num)
                        raise exceptions.ClientRequestException(status_code, error_code, error_msg)
                    elif status_code >= 400 and status_code < 410:
                        self._logger.error('do http request, status code 400~410 error, err:%s, host_url:%s, retry:%d, status_code:%d, sleep_second:%d', resp.text, host_url, retry_num, status_code, retry_num)
                        raise exceptions.ClientRequestException(status_code, error_code, error_msg)
                    else:
                        # Retry
                        self._logger.debug('do http request, retry, host_url:%s, retry:%d, status_code:%d, sleep_second:%d', host_url, retry_num, status_code, retry_num)
                        time.sleep(retry_num)
                        continue
                except requests.exceptions.HTTPError as e:
                    self._logger.error('do http request, http error, err:%s, host_url:%s, retry:%d', e, host_url, retry_num)
                    break
                except requests.exceptions.RequestException as e:
                    self._logger.error('do http request, request failed, err:%s, host_url:%s, retry:%d', e, host_url, retry_num)
        
        raise exceptions.ClientRequestException(status_code, error_code, error_msg)
    
    @property
    def logger(self):
        return self._logger

    def with_app_id(self, app_id):
        self._app_id = app_id

        return self
    
    def with_basic_auth(self, user_name, password):
        self._basic_auth = (user_name, password)

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
