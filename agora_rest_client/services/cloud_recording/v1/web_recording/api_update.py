from agora_rest_client.core import request
from agora_rest_client.services.cloud_recording.v1 import api_update
from agora_rest_client.services.cloud_recording.v1.api import Mode

class WebRecordingConfig(api_update.WebRecordingConfig):
    pass

class RtmpPublishConfig(api_update.RtmpPublishConfig):
    pass

class ClientRequest(request.RequestObject):
    """
    instance of `WebRecordingConfig`
    """
    webRecordingConfig = None

    """
    instance of `RtmpPublishConfig`
    """
    rtmpPublishConfig = None

class RequestPathParamsApiUpdate(api_update.RequestPathParamsApiUpdate):
    pass

class RequestBodyApiUpdate(api_update.RequestBodyApiUpdate):
    pass

class ResponseApiUpdate(api_update.ResponseApiUpdate):
    pass

def web_recording_update(client, resource_id, sid, cname, uid, web_recording_config=None, rtmp_publish_config=None):
    """
    Web recording update

    :param client: WebRecordingClient object
    :param resource_id: resource id, `agora_rest_client.services.cloud_recording.v1.api_update.RequestPathParamsApiUpdate.resource_id`
    :param sid: sid, `agora_rest_client.services.cloud_recording.v1.api_update.RequestPathParamsApiUpdate.sid`
    :param cname: cname, `agora_rest_client.services.cloud_recording.v1.api_update.RequestBodyApiUpdate.cname`
    :param uid: uid, `agora_rest_client.services.cloud_recording.v1.api_update.RequestBodyApiUpdate.uid`
    :param web_recording_config: web recording config, `agora_rest_client.services.cloud_recording.v1.api_update.WebRecordingConfig`
    :param rtmp_publish_config: rtmp publish config, `agora_rest_client.services.cloud_recording.v1.api_update.RtmpPublishConfig`
    :param response_obj: response object
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

    return api_update.api_update(client, request_path_params_obj=request_path_params_obj, request_body_obj=request_body_obj, response_obj=ResponseApiUpdate)
