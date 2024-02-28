from agora_rest_client.services.cloud_recording.v1 import api_acquire
from agora_rest_client.services.cloud_recording.v1.api import Mode

class ClientRequest(api_acquire.ClientRequest):
    pass

class RequestBodyApiAcquire(api_acquire.RequestBodyApiAcquire):
    pass

class ResponseApiAcquire(api_acquire.ResponseApiAcquire):
    pass

def web_recording_acquire(client, cname, uid, resource_expired_hour=72, exclude_resource_ids=[], region_affinity=0, response_type='object', response_obj=ResponseApiAcquire):
    """
    Web recoding acquire

    :param client: WebRecordingClient object
    :param cname: cname, `agora_rest_client.services.cloud_recording.v1.api_acquire.RequestBodyApiAcquire.cname`
    :param uid: uid, `agora_rest_client.services.cloud_recording.v1.api_acquire.RequestBodyApiAcquire.uid`
    :param resource_expired_hour: resource expired hour, `agora_rest_client.services.cloud_recording.v1.api_acquire.ClientRequest.resourceExpiredHour`
    :param exclude_resource_ids: exclude resource ids, `agora_rest_client.services.cloud_recording.v1.api_acquire.ClientRequest.excludeResourceIds`
    :param region_affinity: region affinity, `agora_rest_client.services.cloud_recording.v1.api_acquire.ClientRequest.regionAffinity`
    :param response_obj: response object
    :return: response object ResponseApiResponseApiAcquire
    """
    request_body_obj = RequestBodyApiAcquire({
        'cname': cname,
        'uid': uid,
        'clientRequest': {
            'scene': 1,
            'resourceExpiredHour': resource_expired_hour,
            'excludeResourceIds': exclude_resource_ids,
            'regionAffinity': region_affinity
        }
    })
    
    return api_acquire.api_acquire(client, request_body_obj=request_body_obj, response_type=response_type, response_obj=response_obj)
