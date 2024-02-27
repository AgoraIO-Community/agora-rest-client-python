import logging
import os
from agora_rest_client.core import exceptions
from agora_rest_client.core.domain import RegionArea
from agora_rest_client.services.cloud_recording.v1 import api_acquire
from agora_rest_client.services.cloud_recording.v1 import api_query
from agora_rest_client.services.cloud_recording.v1 import api_start
from agora_rest_client.services.cloud_recording.v1 import api_stop
from agora_rest_client.services.cloud_recording.v1 import api_update_layout
from agora_rest_client.services.cloud_recording.v1 import api_update
from agora_rest_client.services.cloud_recording.v1 import cloud_recording_client

if __name__ == '__main__':
    # Need to set environment variable AGORA_APP_ID
    app_id = os.environ.get('AGORA_APP_ID')
    # Need to set environment variable AGORA_BASIC_AUTH_USER_NAME
    basic_auth_user_name = os.environ.get('AGORA_BASIC_AUTH_USER_NAME')
    # Need to set environment variable AGORA_BASIC_AUTH_PASSWORD
    basic_auth_password = os.environ.get('AGORA_BASIC_AUTH_PASSWORD')

    cname = os.environ.get('AGORA_CNAME')
    uid = os.environ.get('AGORA_UID')
    mode = os.environ.get('AGORA_MODE')
    token = os.environ.get('AGORA_TOKEN')
    storage_config_region = int(os.environ.get('AGORA_STORAGE_CONFIG_REGION'))
    storage_config_vendor = int(os.environ.get('AGORA_STORAGE_CONFIG_VENDOR'))
    storage_config_bucket = os.environ.get('AGORA_STORAGE_CONFIG_BUCKET')
    storage_config_access_key = os.environ.get('AGORA_STORAGE_CONFIG_ACCESS_KEY')
    storage_config_secret_key = os.environ.get('AGORA_STORAGE_CONFIG_SECRET_KEY')

    cloud_recording_client = cloud_recording_client.CloudRecordingClient \
        .new_builder() \
        .with_app_id(app_id) \
        .with_basic_auth(basic_auth_user_name, basic_auth_password) \
        .with_region(RegionArea.CN.value) \
        .with_stream_log(log_level=logging.DEBUG) \
        .with_file_log(path='test.log') \
        .build()

    # Acquire resource
    try:
        request_body_obj = api_acquire.RequestBodyApiAcquire({'cname': cname, 'uid': uid, 'clientRequest': {}})
        response = cloud_recording_client.acquire(request_body_obj)
        cloud_recording_client.logger.info('acquire resource, request_body_obj:%s, response:%s', request_body_obj, response)
    except exceptions.ClientRequestException as e:
        cloud_recording_client.logger.error('acquire resource, request_body_obj:%s, err:%s', request_body_obj, e)
        os._exit(1)

    resource_id = response.resourceId

    # Start recording
    try:
        request_path_params_obj = api_start.RequestPathParamsApiStart({'mode': mode, 'resource_id': resource_id})
        request_body_obj = api_start.RequestBodyApiStart({'cname': cname, 'uid': uid, 'clientRequest': {
            'token': token,
            'storageConfig': {
                'region': storage_config_region,
                'vendor': storage_config_vendor,
                'bucket': storage_config_bucket,
                'accessKey': storage_config_access_key,
                'secretKey': storage_config_secret_key,
            }
        }})
        response = cloud_recording_client.start(request_path_params_obj, request_body_obj)
        cloud_recording_client.logger.info('start recording, request_path_params_obj:%s, request_body_obj:%s, response:%s', request_path_params_obj, request_body_obj, response)
    except exceptions.ClientRequestException as e:
        cloud_recording_client.logger.error('start recording, request_path_params_obj:%s, request_body_obj:%s, err:%s', request_path_params_obj, request_body_obj, e)
        os._exit(1)

    sid = response.sid

    # Query recording
    try:
        request_path_params_obj = api_query.RequestPathParamsApiQuery({'mode': mode, 'resource_id': resource_id, 'sid': sid})
        response = cloud_recording_client.query(request_path_params_obj)
        cloud_recording_client.logger.info('query recording, request_path_params_obj:%s, response:%s', request_path_params_obj, response)
    except exceptions.ClientRequestException as e:
        cloud_recording_client.logger.error('query recording, request_path_params_obj:%s, err:%s', request_path_params_obj, e)
        os._exit(1)

    # Update recording
    try:
        request_path_params_obj = api_update.RequestPathParamsApiUpdate({'mode': mode, 'resource_id': resource_id, 'sid': sid})
        request_body_obj = api_update.RequestBodyApiUpdate({'cname': cname, 'uid': uid, 'clientRequest': {
            'streamSubscribe': {
                'videoUidList': {
                    'subscribeVideoUids': [uid]
                }
            }
        }})
        response = cloud_recording_client.update(request_path_params_obj, request_body_obj)
        cloud_recording_client.logger.info('update recording, request_path_params_obj:%s, request_body_obj:%s, response:%s', request_path_params_obj, request_body_obj, response)
    except exceptions.ClientRequestException as e:
        cloud_recording_client.logger.error('update recording, request_path_params_obj:%s, request_body_obj:%s, err:%s', request_path_params_obj, request_body_obj, e)
        os._exit(1)

    # Update layout recording
    try:
        request_path_params_obj = api_update_layout.RequestPathParamsApiUpdateLayout({'mode': mode, 'resource_id': resource_id, 'sid': sid})
        request_body_obj = api_update_layout.RequestBodyApiUpdateLayout({'cname': cname, 'uid': uid, 'clientRequest': {
            'mixedVideoLayout': 1
        }})
        response = cloud_recording_client.update_layout(request_path_params_obj, request_body_obj)
        cloud_recording_client.logger.info('update layout recording, request_path_params_obj:%s, request_body_obj:%s, response:%s', request_path_params_obj, request_body_obj, response)
    except exceptions.ClientRequestException as e:
        cloud_recording_client.logger.error('update layout recording, request_path_params_obj:%s, request_body_obj:%s, err:%s', request_path_params_obj, request_body_obj, e)
        os._exit(1)

    # Stop recording
    try:
        request_path_params_obj = api_stop.RequestPathParamsApiStop({'mode': mode, 'resource_id': resource_id, 'sid': sid})
        request_body_obj = api_stop.RequestBodyApiStop({'cname': cname, 'uid': uid, 'clientRequest': {}})
        response = cloud_recording_client.stop(request_path_params_obj, request_body_obj)
        cloud_recording_client.logger.info('stop recording, request_path_params_obj:%s, request_body_obj:%s, response:%s', request_path_params_obj, request_body_obj, response)
    except exceptions.ClientRequestException as e:
        cloud_recording_client.logger.error('stop recording, request_path_params_obj:%s, request_body_obj:%s, err:%s', request_path_params_obj, request_body_obj, e)
        os._exit(1)

