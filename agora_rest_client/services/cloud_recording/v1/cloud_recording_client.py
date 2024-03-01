import json
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

        :type: object
        :return: instance of `response_obj`
        """
        try:
            resp = super().call_api(method, url, params=params, post_data=post_data, post_json=post_json, headers=headers, timeout_seconds=timeout_seconds)

            # Request success
            if resp.status_code == 200 or resp.status_code == 201:
                return response_obj(**json.loads(resp.text))

            resp_json = resp.json()
            error_code = resp_json.get(self._error_code_key)
            error_msg = resp_json.get(self._error_msg_key) if resp_json.get(self._error_msg_key) is not None else resp.text

            raise exceptions.ClientRequestException(resp.status_code, error_code, error_msg)
        except Exception as e:
            raise e

    def acquire(self, request_body_obj):
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

        :return: response object ResponseApiAcquire
        """
        return api_acquire(self, request_body_obj)

    def query(self, request_path_params_obj):
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

        :return: response object ResponseApiQuery
        """
        return api_query(self, request_path_params_obj)

    def start(self, request_path_params_obj, request_body_obj):
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

        :return: response object ResponseApiStart
        """
        return api_start(self, request_path_params_obj, request_body_obj)

    def stop(self, request_path_params_obj, request_body_obj):
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

        :return: response object ResponseApiStop
        """
        return api_stop(self, request_path_params_obj, request_body_obj)

    def update(self, request_path_params_obj, request_body_obj):
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

        :return: response object ResponseApiUpdate
        """
        return api_update(self, request_path_params_obj, request_body_obj)

    def update_layout(self, request_path_params_obj, request_body_obj):
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

        :return: response object ResponseApiUpdateLayout
        """
        return api_update_layout(self, request_path_params_obj, request_body_obj)
