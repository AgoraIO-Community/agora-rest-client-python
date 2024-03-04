from agora_rest_client.services.cloud_recording.v1 import api_stop
from agora_rest_client.services.cloud_recording.v1.api import Mode

class RequestPathParamsApiStop(api_stop.RequestPathParamsApiStop):
    pass

class RequestBodyApiStop(api_stop.RequestBodyApiStop):
    pass

class ResponseApiStop(api_stop.ResponseApiStop):
    pass

def mix_recording_stop(client, resource_id, sid, cname, uid, async_stop=False, trace_id=None):
    """
    Mix recording stop
    停止云端录制

    :type client: object
    :param client: MixRecordingClient object

    :type resource_id: str
    :param resource_id: resource id
    :refer: `agora_rest_client.services.cloud_recording.v1.api_stop.RequestPathParamsApiStop.resource_id`

    :type sid: str
    :param sid: sid
    :refer: `agora_rest_client.services.cloud_recording.v1.api_stop.RequestPathParamsApiStop.sid`

    :type cname: str
    :param cname: cname
    :refer: `agora_rest_client.services.cloud_recording.v1.api_stop.RequestBodyApiStop.cname`

    :type uid: str
    :param uid: uid
    :refer: `agora_rest_client.services.cloud_recording.v1.api_stop.RequestBodyApiStop.uid`

    :type async_stop: bool
    :param async_stop: async stop
    :refer: `agora_rest_client.services.cloud_recording.v1.api_stop.ClientRequest.async_stop`

    :type trace_id: string
    :param trace_id: trace id

    :return: response object ResponseApiStop
    """
    request_path_params_obj = RequestPathParamsApiStop(
        mode=Mode.MIX.value,
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

    return api_stop.api_stop(client, request_path_params_obj=request_path_params_obj, request_body_obj=request_body_obj,
                             response_obj=ResponseApiStop, trace_id=trace_id)
