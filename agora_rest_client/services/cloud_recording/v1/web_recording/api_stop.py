from agora_rest_client.services.cloud_recording.v1 import api_stop
from agora_rest_client.services.cloud_recording.v1.api import Mode

class RequestPathParamsApiStop(api_stop.RequestPathParamsApiStop):
    pass

class RequestBodyApiStop(api_stop.RequestBodyApiStop):
    pass

class ResponseApiStop(api_stop.ResponseApiStop):
    pass

def web_recording_stop(client, resource_id, sid, cname, uid, async_stop=False, response_type='object', response_obj=ResponseApiStop):
    """
    Web recording stop

    :param client: WebRecordingClient object
    :param resource_id: resource id, `agora_rest_client.services.cloud_recording.v1.api_stop.RequestPathParamsApiStop.resource_id`
    :param sid: sid, `agora_rest_client.services.cloud_recording.v1.api_stop.RequestPathParamsApiStop.sid`
    :param cname: cname, `agora_rest_client.services.cloud_recording.v1.api_stop.RequestBodyApiStop.cname`
    :param uid: uid, `agora_rest_client.services.cloud_recording.v1.api_stop.RequestBodyApiStop.uid`
    :param async_stop: async stop, `agora_rest_client.services.cloud_recording.v1.api_stop.ClientRequest.async_stop`
    :param response_obj: response object
    :return: response object ResponseApiStop
    """
    request_path_params_obj = RequestPathParamsApiStop({
        'mode': Mode.WEB.value,
        'resource_id': resource_id,
        'sid': sid
    })

    request_body_obj = RequestBodyApiStop({
        'cname': cname,
        'uid': uid,
        'clientRequest': {
            'async_stop': async_stop,
        }
    })

    return api_stop.api_stop(client, request_path_params_obj=request_path_params_obj, request_body_obj=request_body_obj, response_type=response_type, response_obj=response_obj)
