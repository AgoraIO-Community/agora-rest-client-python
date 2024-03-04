from agora_rest_client.services.cloud_recording.v1 import api_query
from agora_rest_client.services.cloud_recording.v1.api import Mode

class RequestPathParamsApiQuery(api_query.RequestPathParamsApiQuery):
    pass

class ResponseApiQuery(api_query.ResponseApiQuery):
    pass

def mix_recording_query(client, resource_id, sid, trace_id=None):
    """
    Mix recording query
    查询云端录制状态

    :type client: object
    :param client: MixRecordingClient object

    :type resource_id: str
    :param resource_id: resource id
    :refer: `agora_rest_client.services.cloud_recording.v1.api_query.RequestPathParamsApiQuery.resource_id`

    :type sid: str
    :param sid: sid
    :refer: `agora_rest_client.services.cloud_recording.v1.api_query.RequestPathParamsApiQuery.sid`

    :type trace_id: string
    :param trace_id: trace id

    :return: response object ResponseApiQuery
    """
    request_path_params_obj = RequestPathParamsApiQuery(
        mode=Mode.MIX.value,
        resource_id=resource_id,
        sid=sid
    )

    return api_query.api_query(client, request_path_params_obj=request_path_params_obj, response_obj=ResponseApiQuery, trace_id=trace_id)
