from agora_rest_client.services.cloud_recording.v1 import api_query
from agora_rest_client.services.cloud_recording.v1.api import Mode

class RequestPathParamsApiQuery(api_query.RequestPathParamsApiQuery):
    pass

class ResponseApiQuery(api_query.ResponseApiQuery):
    pass

def individual_recording_query(client, resource_id, sid):
    """
    Individual recording query

    :type client: object
    :param client: IndividualRecordingClient object
    
    :type resource_id: str
    :param resource_id: resource id, `agora_rest_client.services.cloud_recording.v1.api_query.RequestPathParamsApiQuery.resource_id`
    
    :type sid: str
    :param sid: sid, `agora_rest_client.services.cloud_recording.v1.api_query.RequestPathParamsApiQuery.sid`

    :return: response object ResponseApiQuery
    """
    request_path_params_obj = RequestPathParamsApiQuery(
        mode=Mode.INDIVIDUAL.value,
        resource_id=resource_id,
        sid=sid
    )

    return api_query.api_query(client, request_path_params_obj=request_path_params_obj, response_obj=ResponseApiQuery)
