from agora_rest_client.core import request
from agora_rest_client.services.cloud_recording.v1 import api_start
from agora_rest_client.services.cloud_recording.v1.api import Mode
from agora_rest_client.services.cloud_recording.v1.api import SnapshotType

class StorageConfig(api_start.StorageConfig):
    pass

class RecordingConfig(api_start.RecordingConfig):
    pass

class RecordingFileConfig(api_start.RecordingFileConfig):
    pass

class ClientRequest(request.RequestObject):
    """
    reference to `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest.token`
    """
    token = None

    """
    instance of `StorageConfig`
    """
    storageConfig = None

    """
    instance of `RecordingConfig`
    """
    recordingConfig = None

    """
    instance of `RecordingFileConfig`
    """
    recordingFileConfig = None

class RequestPathParamsApiStart(api_start.RequestPathParamsApiStart):
    pass

class RequestBodyApiStart(api_start.RequestBodyApiStart):
    pass

class ResponseApiStart(api_start.ResponseApiStart):
    pass

def mix_recording_start(client, resource_id, cname, uid, token, storage_config, recording_config=None):
    """
    Mix recording start

    :type client: object
    :param client: MixRecordingClient object
    
    :type resource_id: str
    :param resource_id: resource id, `agora_rest_client.services.cloud_recording.v1.api_start.RequestPathParamsApiStart.resource_id`
    
    :type cname: str
    :param cname: cname, `agora_rest_client.services.cloud_recording.v1.api_start.RequestBodyApiStart.cname`
    
    :type uid: str
    :param uid: uid, `agora_rest_client.services.cloud_recording.v1.api_start.RequestBodyApiStart.uid`
    
    :type token: str
    :param token: token, `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest.token`
    
    :type storage_config: object
    :param storage_config: storage config, `agora_rest_client.services.cloud_recording.v1.api_start.StorageConfig`
    
    :type recording_config: object
    :param recording_config: recording config, `agora_rest_client.services.cloud_recording.v1.api_start.RecordingConfig`
    
    :return: response object ResponseApiStart
    """
    request_path_params_obj = RequestPathParamsApiStart(
        mode=Mode.MIX.value,
        resource_id=resource_id
    )

    request_body_obj = RequestBodyApiStart(
        cname=cname,
        uid=uid,
        clientRequest=ClientRequest(
            token=token,
            storageConfig=storage_config,
            recordingFileConfig=RecordingFileConfig(
                avFileType=['hls', 'mp4']
            )
        )
    )

    if recording_config is not None:
        request_body_obj.clientRequest.recordingConfig = recording_config

    return api_start.api_start(client, request_path_params_obj=request_path_params_obj, request_body_obj=request_body_obj, response_obj=ResponseApiStart)
