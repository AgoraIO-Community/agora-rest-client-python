from agora_rest_client.core import response
from agora_rest_client.services.cloud_recording.v1.cloud_recording_client import CloudRecordingClient
from agora_rest_client.services.cloud_recording.v1.web_recording.api_acquire import web_recording_acquire
from agora_rest_client.services.cloud_recording.v1.web_recording.api_query import web_recording_query
from agora_rest_client.services.cloud_recording.v1.web_recording.api_start import web_recording_start
from agora_rest_client.services.cloud_recording.v1.web_recording.api_start import _web_recording_start
from agora_rest_client.services.cloud_recording.v1.web_recording.api_stop import web_recording_stop
from agora_rest_client.services.cloud_recording.v1.web_recording.api_update import web_recording_update

class WebRecordingClient(CloudRecordingClient):
    """
    Web recording client
    """
    
    def __init__(self):
        super(WebRecordingClient, self).__init__()

    def new_builder():
        return WebRecordingClient()

    def acquire(self, request_body_obj, response_type=response.ResponseType.OBJECT.value):
        return web_recording_acquire(self, request_body_obj, response_type=response_type)

    def query(self, request_path_params_obj, response_type=response.ResponseType.OBJECT.value):
        return web_recording_query(self, request_path_params_obj, response_type=response_type)

    def start(self, resource_id, cname, uid, storageConfig, extensionServiceConfig, response_type=response.ResponseType.OBJECT.value):
        return web_recording_start(self, resource_id, cname, uid, storageConfig, extensionServiceConfig, response_type=response_type)

    def _start(self, request_path_params_obj, request_body_obj, response_type=response.ResponseType.OBJECT.value):
        return _web_recording_start(self, request_path_params_obj, request_body_obj, response_type=response_type)

    def stop(self, request_path_params_obj, request_body_obj, response_type=response.ResponseType.OBJECT.value):
        return web_recording_stop(self, request_path_params_obj, request_body_obj, response_type=response_type)

    def update(self, request_path_params_obj, request_body_obj, response_type=response.ResponseType.OBJECT.value):
        return web_recording_update(self, request_path_params_obj, request_body_obj, response_type=response_type)
