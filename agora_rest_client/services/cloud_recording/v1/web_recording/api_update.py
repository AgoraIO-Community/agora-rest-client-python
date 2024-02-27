from agora_rest_client.services.cloud_recording.v1 import api_update
from agora_rest_client.services.cloud_recording.v1.api import Mode

class ClientRequest(object):
    webRecordingConfig = api_update.WebRecordingConfig()
    rtmpPublishConfig = api_update.RtmpPublishConfig()

class RequestPathParamsApiUpdate(api_update.RequestPathParamsApiUpdate):
    pass

class RequestBodyApiUpdate(api_update.RequestBodyApiUpdate):
    pass

class ResponseApiUpdate(api_update.ResponseApiUpdate):
    pass

def web_recording_update(client, request_path_params_obj, request_body_obj, response_type, response_obj=ResponseApiUpdate):
    request_path_params_obj.mode = Mode.WEB.value

    return api_update.api_update(client, request_path_params_obj=request_path_params_obj, request_body_obj=request_body_obj, response_type=response_type, response_obj=response_obj)
