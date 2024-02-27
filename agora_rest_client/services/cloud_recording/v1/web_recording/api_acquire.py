from agora_rest_client.services.cloud_recording.v1 import api_acquire

class ClientRequest(api_acquire.ClientRequest):
    pass

class RequestBodyApiAcquire(api_acquire.RequestBodyApiAcquire):
    pass

class ResponseApiAcquire(api_acquire.ResponseApiAcquire):
    pass

def web_recording_acquire(client, request_body_obj, response_type, response_obj=ResponseApiAcquire):
    request_body_obj.clientRequest = dict(request_body_obj.clientRequest, **{
        'scene': 1
    })
    
    return api_acquire.api_acquire(client, request_body_obj=request_body_obj, response_type=response_type, response_obj=response_obj)
