from agora_rest_client.core import request
from agora_rest_client.services.cloud_recording.v1 import api_update
from agora_rest_client.services.cloud_recording.v1.api import Mode

class WebRecordingConfig(api_update.WebRecordingConfig):
    pass

class RtmpPublishConfig(api_update.RtmpPublishConfig):
    pass

class ClientRequest(request.RequestObject):
    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update.ClientRequest.webRecordingConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.web_recording.api_update.WebRecordingConfig`
    """
    webRecordingConfig = None

    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update.ClientRequest.rtmpPublishConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.web_recording.api_update.RtmpPublishConfig`
    """
    rtmpPublishConfig = None

class RequestPathParamsApiUpdate(api_update.RequestPathParamsApiUpdate):
    pass

class RequestBodyApiUpdate(api_update.RequestBodyApiUpdate):
    pass

class ResponseApiUpdate(api_update.ResponseApiUpdate):
    pass

def web_recording_update(client, resource_id, sid, cname, uid, web_recording_config=None, rtmp_publish_config=None, trace_id=None):
    """
    Web recording update
    更新云端录制设置

    :type client: object
    :param client: WebRecordingClient object

    :type resource_id: str
    :param resource_id: resource id
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update.RequestPathParamsApiUpdate.resource_id`

    :type sid: str
    :param sid: sid
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update.RequestPathParamsApiUpdate.sid`

    :type cname: str
    :param cname: cname
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update.RequestBodyApiUpdate.cname`

    :type uid: str
    :param uid: uid
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update.RequestBodyApiUpdate.uid`

    :type web_recording_config: object
    :param web_recording_config: web recording config
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update.WebRecordingConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.web_recording.api_update.WebRecordingConfig`

    :type rtmp_publish_config: object
    :param rtmp_publish_config: rtmp publish config
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update.RtmpPublishConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.web_recording.api_update.RtmpPublishConfig`

    :type trace_id: string
    :param trace_id: trace id

    :return: response object ResponseApiUpdate
    """
    request_path_params_obj = RequestPathParamsApiUpdate(
        mode=Mode.WEB.value,
        resource_id=resource_id,
        sid=sid
    )

    request_body_obj = RequestBodyApiUpdate(
        cname=cname,
        uid=uid,
        clientRequest=ClientRequest()
    )

    if web_recording_config is not None:
        request_body_obj.clientRequest.webRecordingConfig = web_recording_config

    if rtmp_publish_config is not None:
        request_body_obj.clientRequest.rtmpPublishConfig = rtmp_publish_config

    return api_update.api_update(client, request_path_params_obj=request_path_params_obj, request_body_obj=request_body_obj,
                                 response_obj=ResponseApiUpdate, trace_id=trace_id)
