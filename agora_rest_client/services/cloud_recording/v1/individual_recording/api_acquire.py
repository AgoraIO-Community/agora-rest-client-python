from agora_rest_client.services.cloud_recording.v1 import api_acquire
from agora_rest_client.services.cloud_recording.v1.api import Scene

class ClientRequest(api_acquire.ClientRequest):
    pass

class RequestBodyApiAcquire(api_acquire.RequestBodyApiAcquire):
    pass

class ResponseApiAcquire(api_acquire.ResponseApiAcquire):
    pass

def individual_recording_acquire(client, cname, uid, enable_postpone_transcoding_mix=False, resource_expired_hour=72, exclude_resource_ids=[], region_affinity=0):
    """
    Individual recording acquire
    获取云端录制资源
    
    :type client: object
    :param client: IndividualRecordingClient object
    
    :type cname: str
    :param cname: cname
    :refer: `agora_rest_client.services.cloud_recording.v1.api_acquire.RequestBodyApiAcquire.cname`
    
    :type uid: str
    :param uid: uid
    :refer: `agora_rest_client.services.cloud_recording.v1.api_acquire.RequestBodyApiAcquire.uid`
    
    :type enable_postpone_transcoding_mix: bool
    :param enable_postpone_transcoding_mix: 开启延时转码或延时混音

    :type resource_expired_hour: int
    :param resource_expired_hour: resource expired hour
    :refer: `agora_rest_client.services.cloud_recording.v1.api_acquire.ClientRequest.resourceExpiredHour`
    
    :type exclude_resource_ids: list
    :param exclude_resource_ids: exclude resource ids
    :refer: `agora_rest_client.services.cloud_recording.v1.api_acquire.ClientRequest.excludeResourceIds`
    
    :type region_affinity: int
    :param region_affinity: region affinity
    :refer: `agora_rest_client.services.cloud_recording.v1.api_acquire.ClientRequest.regionAffinity`
    
    :return: response object ResponseApiAcquire
    """
    request_body_obj = RequestBodyApiAcquire(
        cname=cname,
        uid=uid,
        clientRequest=ClientRequest(
            scene=Scene.INDIVIDUAL_RECORDING_POSTPONE_TRANSCODING_MIX.value if enable_postpone_transcoding_mix else Scene.RTC.value,
            resourceExpiredHour=resource_expired_hour,
            excludeResourceIds=exclude_resource_ids,
            regionAffinity=region_affinity,
    ))

    return api_acquire.api_acquire(client, request_body_obj=request_body_obj, response_obj=ResponseApiAcquire)
