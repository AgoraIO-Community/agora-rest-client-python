from agora_rest_client.services.cloud_recording.v1 import api_stop
from agora_rest_client.services.cloud_recording.v1.api import Mode

class RequestPathParamsApiStop(api_stop.RequestPathParamsApiStop):
    pass

class RequestBodyApiStop(api_stop.RequestBodyApiStop):
    pass

class ResponseApiStop(api_stop.ResponseApiStop):
    pass

def individual_recording_stop(client, resource_id, sid, cname, uid, async_stop=False):
    """
    Individual recording stop

    :type client: object
    :param client: WebRecordingClient object
    
    :type resource_id: str
    :param resource_id: resource id, `agora_rest_client.services.cloud_recording.v1.api_stop.RequestPathParamsApiStop.resource_id`
    
    :type sid: str
    :param sid: sid, `agora_rest_client.services.cloud_recording.v1.api_stop.RequestPathParamsApiStop.sid`
    
    :type cname: str
    :param cname: cname, `agora_rest_client.services.cloud_recording.v1.api_stop.RequestBodyApiStop.cname`
    
    :type uid: str
    :param uid: uid, `agora_rest_client.services.cloud_recording.v1.api_stop.RequestBodyApiStop.uid`
    
    :type async_stop: boolean
    :param async_stop: async stop, `agora_rest_client.services.cloud_recording.v1.api_stop.ClientRequest.async_stop`
    
    :return: response object ResponseApiStop
    """
    request_path_params_obj = RequestPathParamsApiStop(
        mode=Mode.INDIVIDUAL.value,
        resource_id=resource_id,
        sid=sid
    )

    request_body_obj = RequestBodyApiStop(
        cname=cname,
        uid=uid,
        clientRequest=api_stop.ClientRequest(
            async_stop=async_stop
        )
    )

    return api_stop.api_stop(client, request_path_params_obj=request_path_params_obj, request_body_obj=request_body_obj, response_obj=ResponseApiStop)
