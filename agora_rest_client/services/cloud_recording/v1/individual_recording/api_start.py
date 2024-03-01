from agora_rest_client.core import request
from agora_rest_client.services.cloud_recording.v1 import api_start
from agora_rest_client.services.cloud_recording.v1.api import AvFileType
from agora_rest_client.services.cloud_recording.v1.api import Mode
from agora_rest_client.services.cloud_recording.v1.api import SnapshotType

class StorageConfig(api_start.StorageConfig):
    pass

class RecordingConfig(api_start.RecordingConfig):
    pass

class RecordingFileConfig(api_start.RecordingFileConfig):
    pass

class SnapshotConfig(api_start.SnapshotConfig):
    pass

class AppsCollection(api_start.AppsCollection):
    pass

class TranscodeOptions(api_start.TranscodeOptions):
    pass

class ClientRequest(request.RequestObject):
    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest.token`
    """
    token = None

    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest.storageConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.individual_recording.api_start.StorageConfig`
    """
    storageConfig = None

    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest.recordingConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.individual_recording.api_start.RecordingConfig`
    """
    recordingConfig = None

    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest.recordingFileConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.individual_recording.api_start.RecordingFileConfig`
    """
    recordingFileConfig = None

    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest.snapshotConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.individual_recording.api_start.SnapshotConfig`
    """
    snapshotConfig = None

    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest.appsCollection`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.individual_recording.api_start.AppsCollection`
    """
    appsCollection = None

    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest.transcodeOptions`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.individual_recording.api_start.TranscodeOptions`
    """
    transcodeOptions = None

class RequestPathParamsApiStart(api_start.RequestPathParamsApiStart):
    pass

class RequestBodyApiStart(api_start.RequestBodyApiStart):
    pass

class ResponseApiStart(api_start.ResponseApiStart):
    pass

def individual_recording_start(client, resource_id, cname, uid, token, storage_config, recording_config=None,
                               snapshot_type=SnapshotType.SNAPSHOT_AND_RECORDING.value, snapshot_config=None, apps_collection=None, transcode_options=None, trace_id=None):
    """
    Individual recording start
    开始云端录制

    :type client: object
    :param client: IndividualRecordingClientgClient object

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

    :type recording_config: object
    :param recording_config: recording config
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.RecordingConfig`

    :type snapshot_type: int
    :param snapshot_type: 视频截图类型
    :refer: `agora_rest_client.services.cloud_recording.v1.api.SnapshotType`
    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.SnapshotType`

    :type snapshot_config: object
    :param snapshot_config: snapshot config
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.SnapshotConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.individual_recording.api_start.SnapshotConfig`

    :type apps_collection: object
    :param apps_collection: apps collection
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.AppsCollection`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.individual_recording.api_start.AppsCollection`

    :type transcode_options: object
    :param transcode_options: transcode options
    :refer: `agora_rest_client.services.cloud_recording.v1.api_start.TranscodeOptions`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.individual_recording.api_start.TranscodeOptions`

    :type trace_id: string
    :param trace_id: trace id

    :return: response object ResponseApiStart
    """
    request_path_params_obj = RequestPathParamsApiStart(
        mode=Mode.INDIVIDUAL.value,
        resource_id=resource_id
    )

    request_body_obj = RequestBodyApiStart(
        cname=cname,
        uid=uid,
        clientRequest=ClientRequest(
            token=token,
            storageConfig=storage_config,
        )
    )

    if recording_config is not None:
        request_body_obj.clientRequest.recordingConfig = recording_config

    if snapshot_type is SnapshotType.SNAPSHOT_AND_RECORDING.value:
        request_body_obj.clientRequest.recordingFileConfig = RecordingFileConfig(
            avFileType=[AvFileType.HLS.value]
        )

    if snapshot_config is not None:
        request_body_obj.clientRequest.snapshotConfig = snapshot_config

    if apps_collection is not None:
        request_body_obj.clientRequest.appsCollection = apps_collection

    if transcode_options is not None:
        request_body_obj.clientRequest.transcodeOptions = transcode_options

    return api_start.api_start(client, request_path_params_obj=request_path_params_obj, request_body_obj=request_body_obj,
                               response_obj=ResponseApiStart, trace_id=trace_id)
