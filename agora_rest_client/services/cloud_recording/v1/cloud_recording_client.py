import json
import time
import uuid
from agora_rest_client.core import exceptions
from agora_rest_client.core.client import Client
from agora_rest_client.services.cloud_recording.v1.api_acquire import api_acquire
from agora_rest_client.services.cloud_recording.v1.api_query import api_query
from agora_rest_client.services.cloud_recording.v1.api_start import api_start
from agora_rest_client.services.cloud_recording.v1.api_stop import api_stop
from agora_rest_client.services.cloud_recording.v1.api_update import api_update
from agora_rest_client.services.cloud_recording.v1.api_update_layout import api_update_layout

class CloudRecordingClient(Client):
    """
    Cloud recording client
    """

    def __init__(self):
        super(CloudRecordingClient, self).__init__()

        self._error_code_key = 'code'
        self._error_msg_key = 'reason'

    def new_builder():
        return CloudRecordingClient()

    def call_api(self, method, url, params=None, post_data=None, post_json=None, headers=None, timeout_seconds=10, response_obj=None, trace_id=None, is_retry=False):
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

        :type trace_id: string
        :param trace_id: trace id

        :type is_retry: boolean
        :param is_retry: is retry

        :type: object
        :return: instance of `response_obj`
        """
        if trace_id is None:
            trace_id = uuid.uuid1()

        status_code = None
        error_code = None
        error_msg = None
        http_retry_count = self._http_retry_count if is_retry else 1

        # Retry
        for retry in range(http_retry_count):
            retry_num = retry + 1

            try:
                resp = super().call_api(method, url, params=params, post_data=post_data, post_json=post_json, headers=headers, timeout_seconds=timeout_seconds, trace_id=trace_id)
                status_code = resp.status_code

                self._logger.debug('call api, trace_id:%s, url:%s, is_retry:%s, http_retry_count:%d, retry_num:%d, status_code:%s', trace_id, url, is_retry, http_retry_count, retry_num, status_code)

                # Request success
                if status_code == 200 or status_code == 201:
                    return response_obj(**json.loads(resp.text))

                try:
                    resp_json = resp.json()
                    error_code = resp_json.get(self._error_code_key)
                    error_msg = resp_json.get(self._error_msg_key) if resp_json.get(self._error_msg_key) is not None else resp.text
                except Exception as e:
                    error_msg = resp.text

                # Request failed
                # No need to retry
                if status_code >= 400 and status_code < 410:
                    self._logger.error('call api, no retry, trace_id:%s, url:%s, retry_num:%d, status_code:%s, error_code:%s, error_msg:%s', trace_id, url, retry_num, status_code, error_code, error_msg)
                    raise exceptions.ServiceResponseException(status_code, error_code, error_msg)
            except exceptions.ClientTimeoutException as e:
                error_msg = '%s' % e
                self._logger.error('call api, timeout, trace_id:%s, url:%s, retry_num:%d', trace_id, url, retry_num)
            except exceptions.ClientRequestException as e:
                error_msg = '%s' % e
                self._logger.error('call api, request failed, err:%s, trace_id:%s, url:%s, retry_num:%d', e, trace_id, url, retry_num)

            if is_retry:
                # Retry, sleep
                sleep_second = retry_num
                time.sleep(sleep_second)
                self._logger.debug('call api, retry, trace_id:%s, url:%s, retry_num:%d, status_code:%s, error_code:%s, error_msg:%s, sleep_second:%d', trace_id, url, retry_num, status_code, error_code, error_msg, sleep_second)

        raise exceptions.ClientRequestException(status_code, error_code, error_msg)

    def acquire(self, request_body_obj, trace_id=None):
        """
        Acquire a resource id
        获取云端录制资源

        :type client: object
        :param client: CloudRecordingClient object

        :type request_body_obj: object
        :param request_body_obj: request body object
        :value: instance of `agora_rest_client.services.cloud_recording.v1.api_acquire.RequestBodyApiAcquire`

        :type response_obj: object
        :param response_obj: response object
        :value: instance of `agora_rest_client.services.cloud_recording.v1.api_acquire.ResponseApiAcquire`

        :type trace_id: string
        :param trace_id: trace id

        :return: response object ResponseApiAcquire
        """
        return api_acquire(self, request_body_obj, trace_id=trace_id)

    def query(self, request_path_params_obj, trace_id=None):
        """
        Query the recording status
        查询云端录制状态

        :type client: object
        :param client: CloudRecordingClient object

        :type request_path_params_obj: object
        :param request_path_params_obj: request path params object
        :value: instance of `agora_rest_client.services.cloud_recording.v1.api_query.RequestPathParamsApiQuery`

        :type response_obj: object
        :param response_obj: response object
        :value: instance of `agora_rest_client.services.cloud_recording.v1.api_query.ResponseApiQuery`

        :type trace_id: string
        :param trace_id: trace id

        :return: response object ResponseApiQuery
        """
        return api_query(self, request_path_params_obj, trace_id=trace_id)

    def start(self, request_path_params_obj, request_body_obj, trace_id=None):
        """
        Start recording
        开始云端录制

        :type client: object
        :param client: CloudRecordingClient object

        :type request_path_params_obj: object
        :param request_path_params_obj: request path params object
        :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.RequestPathParamsApiStart`

        :type request_body_obj: object
        :param request_body_obj: request body object
        :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.RequestBodyApiStart`

        :type response_obj: object
        :param response_obj: response object
        :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.ResponseApiStart`

        :type trace_id: string
        :param trace_id: trace id

        :return: response object ResponseApiStart
        """
        return api_start(self, request_path_params_obj, request_body_obj, trace_id=trace_id)

    def stop(self, request_path_params_obj, request_body_obj, trace_id=None):
        """
        Stop recording
        停止云端录制

        :type client: object
        :param client: CloudRecordingClient object

        :type request_path_params_obj: object
        :param request_path_params_obj: request path params object
        :value: instance of `agora_rest_client.services.cloud_recording.v1.api_stop.RequestPathParamsApiStop`

        :type request_body_obj: object
        :param request_body_obj: request body object
        :value: instance of `agora_rest_client.services.cloud_recording.v1.api_stop.RequestBodyApiStop`

        :type response_obj: object
        :param response_obj: response object
        :value: instance of `agora_rest_client.services.cloud_recording.v1.api_stop.ResponseApiStop`

        :type trace_id: string
        :param trace_id: trace id

        :return: response object ResponseApiStop
        """
        return api_stop(self, request_path_params_obj, request_body_obj, trace_id=trace_id)

    def update(self, request_path_params_obj, request_body_obj, trace_id=None):
        """
        Update recording
        更新云端录制设置

        :type client: object
        :param client: CloudRecordingClient object

        :type request_path_params_obj: object
        :param request_path_params_obj: request path params object
        :value: instance of `agora_rest_client.services.cloud_recording.v1.api_update.RequestPathParamsApiUpdate`

        :type request_body_obj: object
        :param request_body_obj: request body object
        :value: instance of `agora_rest_client.services.cloud_recording.v1.api_update.RequestBodyApiUpdate`

        :type response_obj: object
        :param response_obj: response object
        :value: instance of `agora_rest_client.services.cloud_recording.v1.api_update.ResponseApiUpdate`

        :type trace_id: string
        :param trace_id: trace id

        :return: response object ResponseApiUpdate
        """
        return api_update(self, request_path_params_obj, request_body_obj, trace_id=trace_id)

    def update_layout(self, request_path_params_obj, request_body_obj, trace_id=None):
        """
        Update layout of the recording
        更新云端录制合流布局

        :type client: object
        :param client: CloudRecordingClient object

        :type request_path_params_obj: object
        :param request_path_params_obj: request path params object
        :value: instance of `agora_rest_client.services.cloud_recording.v1.api_update_layout.RequestPathParamsApiUpdateLayout`

        :type request_body_obj: object
        :param request_body_obj: request body object
        :value: instance of `agora_rest_client.services.cloud_recording.v1.api_update_layout.RequestBodyApiUpdateLayout`

        :type response_obj: object
        :param response_obj: response object
        :value: instance of `agora_rest_client.services.cloud_recording.v1.api_update_layout.ResponseApiUpdateLayout`

        :type trace_id: string
        :param trace_id: trace id

        :return: response object ResponseApiUpdateLayout
        """
        return api_update_layout(self, request_path_params_obj, request_body_obj, trace_id=trace_id)
