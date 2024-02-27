import logging
import os
from agora_rest_client.core import exceptions
from agora_rest_client.core.domain import RegionArea
from agora_rest_client.services.cloud_recording.v1.api import Mode
from agora_rest_client.services.cloud_recording.v1.api_stop import RequestBodyApiStop
from agora_rest_client.services.cloud_recording.v1.api_stop import RequestPathParamsApiStop
from agora_rest_client.services.cloud_recording.v1.cloud_recording_client import CloudRecordingClient

if __name__ == '__main__':
    # Need to set environment variable AGORA_APP_ID
    app_id = os.environ.get('AGORA_APP_ID')
    # Need to set environment variable AGORA_BASIC_AUTH_USER_NAME
    basic_auth_user_name = os.environ.get('AGORA_BASIC_AUTH_USER_NAME')
    # Need to set environment variable AGORA_BASIC_AUTH_PASSWORD
    basic_auth_password = os.environ.get('AGORA_BASIC_AUTH_PASSWORD')

    mode = Mode.INDIVIDUAL.value
    resource_id = 'resource_id'
    sid = 'sid'
    cname = 'cname'
    uid = 'uid'
    clientRequest = {'async_stop': False}

    cloud_recording_client = CloudRecordingClient \
        .new_builder() \
        .with_app_id(app_id) \
        .with_basic_auth(basic_auth_user_name, basic_auth_password) \
        .with_region(RegionArea.CN.value) \
        .with_stream_log(log_level=logging.DEBUG) \
        .with_file_log(path='test.log') \
        .build()
    
    try:
        request_path_params_obj = RequestPathParamsApiStop({'mode': mode, 'resource_id': resource_id, 'sid': sid})
        request_body_obj = RequestBodyApiStop({'cname': cname, 'uid': uid, 'clientRequest': clientRequest})
        response = cloud_recording_client.stop(request_path_params_obj, request_body_obj)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.error_code)
        print(e.error_msg)
