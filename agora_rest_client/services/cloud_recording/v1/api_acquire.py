from agora_rest_client.core import utils

class ClientRequest(object):
    """ 云端录制资源使用场景
    0: 实时音视频录制. 
    1: 页面录制. 
    2: 单流录制模式, 且开启延时转码或延时混音.
    """
    scene = None
    resourceExpiredHour = None
    excludeResourceIds = []
    regionAffinity = None

class RequestBodyApiAcquire(object):
    cname = None
    uid = None
    clientRequest = ClientRequest()

    def __init__(self, d):
        self.__dict__.update(d)

    def __str__(self):
        return ",".join(["{}={}".format(k, v) for k, v in self.__dict__.items()])

class ResponseApiAcquire(object):
    cname = None
    uid = None
    resourceId = None

    def __init__(self, d):
        self.__dict__.update(d)

    def __str__(self):
        return ",".join(["{}={}".format(k, v) for k, v in self.__dict__.items()])

def api_acquire(client, request_body_obj, response_type, response_obj=ResponseApiAcquire):
    """
    :param client: CloudRecordingClient object
    :param request_body_obj: request object RequestBodyApiAcquire
    :param response_type: response type
    :param response_obj: response object
    :return: response object ResponseApiAcquire
    """
    url = '/v1/apps/{}/cloud_recording/acquire'.format(client.app_id)
    client.logger.debug("url:%s", url)

    return client.call_api('POST', url, post_json=utils.to_json(request_body_obj), response_type=response_type, response_obj=response_obj)
