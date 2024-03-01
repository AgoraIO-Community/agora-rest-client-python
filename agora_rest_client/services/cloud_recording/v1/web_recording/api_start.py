from agora_rest_client.core import request
from agora_rest_client.services.cloud_recording.v1 import api_start
from agora_rest_client.services.cloud_recording.v1.api import AvFileType
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
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest.storageConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.web_recording.api_start.StorageConfig`
    """
    storageConfig = None

    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest.recordingFileConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.web_recording.api_start.RecordingFileConfig`
    """
    recordingFileConfig = None

    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest.extensionServiceConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.web_recording.api_start.ExtensionServiceConfig`
    """
    extensionServiceConfig = None

class RequestPathParamsApiStart(api_start.RequestPathParamsApiStart):
    pass

class RequestBodyApiStart(api_start.RequestBodyApiStart):
    pass

class ResponseApiStart(api_start.ResponseApiStart):
    pass

def web_recording_start(client, resource_id, cname, uid, storage_config, extension_service_config, trace_id=None):
    """
    Web recording start
    开始云端录制

    :type client: object
    :param client: WebRecordingClient object

    :type resource_id: str
    :param resource_id: resource id
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.RequestPathParamsApiStart.resource_id`

    :type cname: str
    :param cname: cname
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.RequestBodyApiStart.cname`

    :type uid: str
    :param uid: uid
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.RequestBodyApiStart.uid`

    :type storage_config: object
    :param storage_config: storage config
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.StorageConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.web_recording.api_start.StorageConfig`

    :type extension_service_config: object
    :param extension_service_config: extension service config
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.ExtensionServiceConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.web_recording.api_start.ExtensionServiceConfig`

    :type trace_id: string
    :param trace_id: trace id

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
                avFileType=[AvFileType.HLS.value, AvFileType.MP4.value]
            ),
            extensionServiceConfig=extension_service_config
        )
    )

    return api_start.api_start(client, request_path_params_obj=request_path_params_obj, request_body_obj=request_body_obj,
                               response_obj=ResponseApiStart, trace_id=trace_id)
