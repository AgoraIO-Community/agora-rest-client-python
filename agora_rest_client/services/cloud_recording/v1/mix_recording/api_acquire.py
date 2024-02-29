from agora_rest_client.services.cloud_recording.v1 import api_acquire
from agora_rest_client.services.cloud_recording.v1.api import Scene

class ClientRequest(api_acquire.ClientRequest):
    pass

class RequestBodyApiAcquire(api_acquire.RequestBodyApiAcquire):
    pass

class ResponseApiAcquire(api_acquire.ResponseApiAcquire):
    pass

def mix_recording_acquire(client, cname, uid, resource_expired_hour=72, exclude_resource_ids=[], region_affinity=0):
    """
    Mix recording acquire

    :type client: object
    :param client: MixRecordingClient object
    
    :type cname: str
    :param cname: cname, `agora_rest_client.services.cloud_recording.v1.api_acquire.RequestBodyApiAcquire.cname`
    
    :type uid: str
    :param uid: uid, `agora_rest_client.services.cloud_recording.v1.api_acquire.RequestBodyApiAcquire.uid`
    
    :type resource_expired_hour: int
    :param resource_expired_hour: resource expired hour, `agora_rest_client.services.cloud_recording.v1.api_acquire.ClientRequest.resourceExpiredHour`
    
    :type exclude_resource_ids: list
    :param exclude_resource_ids: exclude resource ids, `agora_rest_client.services.cloud_recording.v1.api_acquire.ClientRequest.excludeResourceIds`
    
    :type region_affinity: int
    :param region_affinity: region affinity, `agora_rest_client.services.cloud_recording.v1.api_acquire.ClientRequest.regionAffinity`
    
    :return: response object ResponseApiAcquire
    """
    request_body_obj = RequestBodyApiAcquire(
        cname=cname,
        uid=uid,
        clientRequest=ClientRequest(
            scene=Scene.RTC.value,
            resourceExpiredHour=resource_expired_hour,
            excludeResourceIds=exclude_resource_ids,
            regionAffinity=region_affinity,
    ))

    return api_acquire.api_acquire(client, request_body_obj=request_body_obj, response_obj=ResponseApiAcquire)
