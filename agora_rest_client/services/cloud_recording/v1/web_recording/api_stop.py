from agora_rest_client.services.cloud_recording.v1 import api_stop
from agora_rest_client.services.cloud_recording.v1.api import Mode

class RequestPathParamsApiStop(api_stop.RequestPathParamsApiStop):
    pass

class RequestBodyApiStop(api_stop.RequestBodyApiStop):
    pass

class ResponseApiStop(api_stop.ResponseApiStop):
    pass

def web_recording_stop(client, request_path_params_obj, request_body_obj, response_type, response_obj=ResponseApiStop):
    request_path_params_obj.mode = Mode.WEB.value

    return api_stop.api_stop(client, request_path_params_obj=request_path_params_obj, request_body_obj=request_body_obj, response_type=response_type, response_obj=response_obj)
