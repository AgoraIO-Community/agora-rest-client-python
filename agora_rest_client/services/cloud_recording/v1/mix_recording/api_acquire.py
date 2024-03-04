from agora_rest_client.services.cloud_recording.v1 import api_acquire
from agora_rest_client.services.cloud_recording.v1.api import Scene

class ClientRequest(api_acquire.ClientRequest):
    pass

class RequestBodyApiAcquire(api_acquire.RequestBodyApiAcquire):
    pass

class ResponseApiAcquire(api_acquire.ResponseApiAcquire):
    pass

def mix_recording_acquire(client, cname, uid, resource_expired_hour=None, exclude_resource_ids=None, region_affinity=None, trace_id=None):
    """
    Mix recording acquire
    获取云端录制资源

    :type client: object
    :param client: MixRecordingClient object

    :type cname: str
    :param cname: cname
    :refer: `agora_rest_client.services.cloud_recording.v1.api_acquire.RequestBodyApiAcquire.cname`

    :type uid: str
    :param uid: uid
    :refer: `agora_rest_client.services.cloud_recording.v1.api_acquire.RequestBodyApiAcquire.uid`

    :type resource_expired_hour: int
    :param resource_expired_hour: resource expired hour
    :refer: `agora_rest_client.services.cloud_recording.v1.api_acquire.ClientRequest.resourceExpiredHour`

    :type exclude_resource_ids: list
    :param exclude_resource_ids: exclude resource ids
    :refer: `agora_rest_client.services.cloud_recording.v1.api_acquire.ClientRequest.excludeResourceIds`

    :type region_affinity: int
    :param region_affinity: region affinity
    :refer: `agora_rest_client.services.cloud_recording.v1.api_acquire.ClientRequest.regionAffinity`
    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.RegionAffinity`

    :type trace_id: string
    :param trace_id: trace id

    :return: response object ResponseApiAcquire
    """
    request_body_obj = RequestBodyApiAcquire(
        cname=cname,
        uid=uid,
        clientRequest=ClientRequest(
            scene=Scene.RTC.value
    ))

    if resource_expired_hour is not None:
        request_body_obj.clientRequest.resourceExpiredHour = resource_expired_hour

    if exclude_resource_ids is not None:
        request_body_obj.clientRequest.excludeResourceIds = exclude_resource_ids

    if region_affinity is not None:
        request_body_obj.clientRequest.regionAffinity = region_affinity

    return api_acquire.api_acquire(client, request_body_obj=request_body_obj, response_obj=ResponseApiAcquire, trace_id=trace_id)
