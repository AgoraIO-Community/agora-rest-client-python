from agora_rest_client.services.cloud_recording.v1 import api_query
from agora_rest_client.services.cloud_recording.v1.api import Mode

class RequestPathParamsApiQuery(api_query.RequestPathParamsApiQuery):
    pass

class ResponseApiQuery(api_query.ResponseApiQuery):
    pass

def web_recording_query(client, request_path_params_obj, response_type, response_obj=ResponseApiQuery):
    request_path_params_obj.mode = Mode.WEB.value

    return api_query.api_query(client, request_path_params_obj=request_path_params_obj, response_type=response_type, response_obj=response_obj)
