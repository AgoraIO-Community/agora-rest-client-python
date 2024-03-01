from agora_rest_client.core import request
from agora_rest_client.services.cloud_recording.v1 import api_start
from agora_rest_client.services.cloud_recording.v1.api import AvFileType
from agora_rest_client.services.cloud_recording.v1.api import Mode

class StorageConfig(api_start.StorageConfig):
    pass

class RecordingConfig(api_start.RecordingConfig):
    pass

class RecordingFileConfig(api_start.RecordingFileConfig):
    pass

class ClientRequest(request.RequestObject):
    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest.token`
    """
    token = None

    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest.storageConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.mix_recording.api_start.StorageConfig`
    """
    storageConfig = None

    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest.recordingConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.mix_recording.api_start.RecordingConfig`
    """
    recordingConfig = None

    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest.recordingConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.mix_recording.api_start.RecordingFileConfig`
    """
    recordingFileConfig = None

class RequestPathParamsApiStart(api_start.RequestPathParamsApiStart):
    pass

class RequestBodyApiStart(api_start.RequestBodyApiStart):
    pass

class ResponseApiStart(api_start.ResponseApiStart):
    pass

def mix_recording_start(client, resource_id, cname, uid, token, storage_config, recording_config=None, trace_id=None):
    """
    Mix recording start
    开始云端录制

    :type client: object
    :param client: MixRecordingClient object

    :type resource_id: str
    :param resource_id: resource id
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.RequestPathParamsApiStart.resource_id`

    :type cname: str
    :param cname: cname
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.RequestBodyApiStart.cname`

    :type uid: str
    :param uid: uid
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.RequestBodyApiStart.uid`

    :type token: str
    :param token: token
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest.token`

    :type storage_config: object
    :param storage_config: storage config
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.StorageConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.mix_recording.api_start.StorageConfig`

    :type recording_config: object
    :param recording_config: recording config
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.RecordingConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.mix_recording.api_start.RecordingConfig`

    :type trace_id: string
    :param trace_id: trace id

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
                avFileType=[AvFileType.HLS.value, AvFileType.MP4.value]
            )
        )
    )

    if recording_config is not None:
        request_body_obj.clientRequest.recordingConfig = recording_config

    return api_start.api_start(client, request_path_params_obj=request_path_params_obj, request_body_obj=request_body_obj,
                               response_obj=ResponseApiStart, trace_id=trace_id)
