from agora_rest_client.services.cloud_recording.v1 import api_start
from agora_rest_client.services.cloud_recording.v1.api import Mode

class ClientRequest(object):
    storageConfig = api_start.StorageConfig()
    recordingFileConfig = api_start.RecordingFileConfig()
    extensionServiceConfig = api_start.ExtensionServiceConfig()

class RequestPathParamsApiStart(api_start.RequestPathParamsApiStart):
    pass

class RequestBodyApiStart(api_start.RequestBodyApiStart):
    pass

class ResponseApiStart(api_start.ResponseApiStart):
    pass

def web_recording_start(client, resource_id, cname, uid, storageConfig, extensionServiceConfig, response_type, response_obj=ResponseApiStart):
    """
    Web recording start

    :param client: WebRecordingClient object
    :param resource_id: resource id
    :param cname: cname
    :param uid: uid
    :param storageConfig: storage config, `agora_rest_client.services.cloud_recording.v1.api_start.StorageConfig`
    :param extensionServiceConfig: extension service config, `agora_rest_client.services.cloud_recording.v1.api_start.ExtensionServiceConfig`
    :param response_type: response type, `agora_rest_client.core.response.ResponseType`
    :param response_obj: response object
    :return: response object ResponseApiStart
    """
    request_path_params_obj = RequestPathParamsApiStart({
        'mode': Mode.WEB.value,
        'resource_id': resource_id
    })

    request_body_obj = RequestBodyApiStart({
        'cname': cname,
        'uid': uid,
        'clientRequest': {
            'storageConfig': storageConfig,
            'recordingFileConfig': {
                'avFileType': ['hls', 'mp4']
            },
            'extensionServiceConfig': extensionServiceConfig
        }
    })

    request_body_obj.clientRequest = dict(request_body_obj.clientRequest, **{
        'recordingFileConfig': {
            'avFileType': ['hls', 'mp4']
        }
    })

    return api_start.api_start(client, request_path_params_obj=request_path_params_obj, request_body_obj=request_body_obj, response_type=response_type, response_obj=response_obj)

def _web_recording_start(client, request_path_params_obj, request_body_obj, response_type, response_obj=ResponseApiStart):
    request_path_params_obj.mode = Mode.WEB.value
    request_body_obj.clientRequest = dict(request_body_obj.clientRequest, **{
        'recordingFileConfig': {
            'avFileType': ['hls', 'mp4']
        }
    })

    return api_start.api_start(client, request_path_params_obj=request_path_params_obj, request_body_obj=request_body_obj, response_type=response_type, response_obj=response_obj)
