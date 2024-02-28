from agora_rest_client.core import request
from agora_rest_client.services.cloud_recording.v1 import api_update
from agora_rest_client.services.cloud_recording.v1.api import Mode

class AudioUidList(api_update.AudioUidList):
    pass

class VideoUidList(api_update.VideoUidList):
    pass

class StreamSubscribe(api_update.StreamSubscribe):
    pass

class ClientRequest(request.RequestObject):
    """
    instance of `StreamSubscribe`
    """
    streamSubscribe = None

class RequestPathParamsApiUpdate(api_update.RequestPathParamsApiUpdate):
    pass

class RequestBodyApiUpdate(api_update.RequestBodyApiUpdate):
    pass

class ResponseApiUpdate(api_update.ResponseApiUpdate):
    pass

def individual_recording_update(client, resource_id, sid, cname, uid, stream_subscribe=None):
    """
    Individual recording update

    :type client: object
    :param client: WebRecordingClient object
    
    :type resource_id: str
    :param resource_id: resource id, `agora_rest_client.services.cloud_recording.v1.api_update.RequestPathParamsApiUpdate.resource_id`
    
    :type sid: str
    :param sid: sid, `agora_rest_client.services.cloud_recording.v1.api_update.RequestPathParamsApiUpdate.sid`
    
    :type cname: str
    :param cname: cname, `agora_rest_client.services.cloud_recording.v1.api_update.RequestBodyApiUpdate.cname`
    
    :type uid: str
    :param uid: uid, `agora_rest_client.services.cloud_recording.v1.api_update.RequestBodyApiUpdate.uid`
    
    :type stream_subscribe: object
    :param stream_subscribe: stream subscribe, `agora_rest_client.services.cloud_recording.v1.api_update.StreamSubscribe`
    
    :return: response object ResponseApiUpdate
    """
    request_path_params_obj = RequestPathParamsApiUpdate(
        mode=Mode.INDIVIDUAL.value,
        resource_id=resource_id,
        sid=sid
    )

    request_body_obj = RequestBodyApiUpdate(
        cname=cname,
        uid=uid,
        clientRequest=ClientRequest()
    )

    if stream_subscribe is not None:
        request_body_obj.clientRequest.streamSubscribe = stream_subscribe

    return api_update.api_update(client, request_path_params_obj=request_path_params_obj, request_body_obj=request_body_obj, response_obj=ResponseApiUpdate)
