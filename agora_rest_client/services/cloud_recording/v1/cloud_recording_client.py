from agora_rest_client.core import response
from agora_rest_client.core.client import Client
from agora_rest_client.services.cloud_recording.v1.api_acquire import api_acquire
from agora_rest_client.services.cloud_recording.v1.api_query import api_query
from agora_rest_client.services.cloud_recording.v1.api_start import api_start
from agora_rest_client.services.cloud_recording.v1.api_stop import api_stop
from agora_rest_client.services.cloud_recording.v1.api_update import api_update
from agora_rest_client.services.cloud_recording.v1.api_update_layout import api_update_layout

class CloudRecordingClient(Client):
    def __init__(self):
        super(CloudRecordingClient, self).__init__()

        self._error_code_key = 'code'
        self._error_msg_key = 'reason'

    def new_builder():
        return CloudRecordingClient()

    def acquire(self, request_body_obj, response_type=response.ResponseType.OBJECT.value):
        return api_acquire(self, request_body_obj, response_type=response_type)

    def query(self, request_path_params_obj, response_type=response.ResponseType.OBJECT.value):
        return api_query(self, request_path_params_obj, response_type=response_type)

    def start(self, request_path_params_obj, request_body_obj, response_type=response.ResponseType.OBJECT.value):
        return api_start(self, request_path_params_obj, request_body_obj, response_type=response_type)

    def stop(self, request_path_params_obj, request_body_obj, response_type=response.ResponseType.OBJECT.value):
        return api_stop(self, request_path_params_obj, request_body_obj, response_type=response_type)

    def update(self, request_path_params_obj, request_body_obj, response_type=response.ResponseType.OBJECT.value):
        return api_update(self, request_path_params_obj, request_body_obj, response_type=response_type)

    def update_layout(self, request_path_params_obj, request_body_obj, response_type=response.ResponseType.OBJECT.value):
        return api_update_layout(self, request_path_params_obj, request_body_obj, response_type=response_type)
