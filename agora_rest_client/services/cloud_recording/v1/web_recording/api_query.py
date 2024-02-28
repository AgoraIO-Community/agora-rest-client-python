from agora_rest_client.services.cloud_recording.v1 import api_query
from agora_rest_client.services.cloud_recording.v1.api import Mode

class RequestPathParamsApiQuery(api_query.RequestPathParamsApiQuery):
    pass

class ResponseApiQuery(api_query.ResponseApiQuery):
    pass

def web_recording_query(client, resource_id, sid, response_type, response_obj=ResponseApiQuery):
    """
    Web recording query

    :param client: WebRecordingClient object
    :param resource_id: resource id, `agora_rest_client.services.cloud_recording.v1.api_query.RequestPathParamsApiQuery.resource_id`
    :param sid: sid, `agora_rest_client.services.cloud_recording.v1.api_query.RequestPathParamsApiQuery.sid`
    """
    request_path_params_obj = RequestPathParamsApiQuery({
        'mode': Mode.WEB.value,
        'resource_id': resource_id,
        'sid': sid
    })

    return api_query.api_query(client, request_path_params_obj=request_path_params_obj, response_type=response_type, response_obj=response_obj)
