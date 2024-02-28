from agora_rest_client.core import request
from agora_rest_client.services.cloud_recording.v1 import api_start
from agora_rest_client.services.cloud_recording.v1.api import Mode

class StorageConfig(api_start.StorageConfig):
    pass

class RecordingFileConfig(api_start.RecordingFileConfig):
    pass

class ExtensionServiceConfig(api_start.ExtensionServiceConfig):
    pass

class ExtensionServices(api_start.ExtensionServices):
    pass

class ServiceParam(api_start.ServiceParam):
    pass

class ClientRequest(request.RequestObject):
    """
    instance of `StorageConfig`
    """
    storageConfig = None

    """
    instance of `RecordingFileConfig`
    """
    recordingFileConfig = None

    """
    instance of `ExtensionServiceConfig`
    """
    extensionServiceConfig = None

class RequestPathParamsApiStart(api_start.RequestPathParamsApiStart):
    pass

class RequestBodyApiStart(api_start.RequestBodyApiStart):
    pass

class ResponseApiStart(api_start.ResponseApiStart):
    pass

def web_recording_start(client, resource_id, cname, uid, storage_config, extension_service_config):
    """
    Web recording start

    :type client: object
    :param client: WebRecordingClient object
    
    :type resource_id: str
    :param resource_id: resource id, `agora_rest_client.services.cloud_recording.v1.api_start.RequestPathParamsApiStart.resource_id`
    
    :type cname: str
    :param cname: cname, `agora_rest_client.services.cloud_recording.v1.api_start.RequestBodyApiStart.cname`
    
    :type uid: str
    :param uid: uid, `agora_rest_client.services.cloud_recording.v1.api_start.RequestBodyApiStart.uid`
    
    :type storage_config: object
    :param storage_config: storage config, `agora_rest_client.services.cloud_recording.v1.api_start.StorageConfig`
    
    :type extension_service_config: object
    :param extension_service_config: extension service config, `agora_rest_client.services.cloud_recording.v1.api_start.ExtensionServiceConfig`
    
    :return: response object ResponseApiStart
    """
    request_path_params_obj = RequestPathParamsApiStart(
        mode=Mode.WEB.value,
        resource_id=resource_id
    )

    request_body_obj = RequestBodyApiStart(
        cname=cname,
        uid=uid,
        clientRequest=ClientRequest(
            storageConfig=storage_config,
            recordingFileConfig=RecordingFileConfig(
                avFileType=['hls', 'mp4']
            ),
            extensionServiceConfig=extension_service_config
        )
    )

    return api_start.api_start(client, request_path_params_obj=request_path_params_obj, request_body_obj=request_body_obj, response_obj=ResponseApiStart)
