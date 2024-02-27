from agora_rest_client.core import utils

class AudioUidList(object):
    subscribeAudioUids = []
    unsubscribeAudioUids = []

class VideoUidList(object):
    subscribeVideoUids = []
    unsunscribeVideoUids = []

class StreamSubscribe(object):
    audioUidList = AudioUidList()
    videoUidList = VideoUidList()

class WebRecordingConfig(object):
    onhold = None

class Outputs(object):
    rtmpUrl = None

class RtmpPublishConfig(object):
    outputs = [Outputs()]

class ClientRequest(object):
    streamSubscribe = StreamSubscribe()
    webRecordingConfig = WebRecordingConfig()
    rtmpPublishConfig = RtmpPublishConfig()

class Payload(object):
    uploadingStatus = None
    
class ExtensionServiceState(object):
    payload = Payload()
    serviceName = None

class ServerResponse(object):
    extensionServiceState = [ExtensionServiceState()]

class RequestPathParamsApiUpdate(object):
    # 录制模式, 参考 Mode 枚举类. 传入字符串, 如 Mode.INDIVIDUAL.value
    mode = None
    # 通过 acquire 请求获取到的 Resource ID
    resource_id = None
    # 通过 start 获取的录制 ID
    sid = None

    def __init__(self, d):
        self.__dict__.update(d)

    def __str__(self):
        return ",".join(["{}={}".format(k, v) for k, v in self.__dict__.items()])

class RequestBodyApiUpdate(object):
    cname = None
    uid = None
    clientRequest = ClientRequest()

    def __init__(self, d):
        self.__dict__.update(d)

    def __str__(self):
        return ",".join(["{}={}".format(k, v) for k, v in self.__dict__.items()])

class ResponseApiUpdate(object):
    cname = None
    uid = None
    resourceId = None
    sid = None
    
    def __init__(self, d):
        self.__dict__.update(d)

    def __str__(self):
        return ",".join(["{}={}".format(k, v) for k, v in self.__dict__.items()])

def api_update(client, request_path_params_obj, request_body_obj, response_type, response_obj=ResponseApiUpdate):
    """
    :param client: CloudRecordingClient object
    :param request_path_params_obj: request object RequestPathParamsApiUpdate
    :param request_body_obj: request object RequestBodyApiUpdate
    :param response_type: response type
    :param response_obj: response object
    :return: response object ResponseApiUpdate
    """
    url = '/v1/apps/{}/cloud_recording/resourceid/{}/sid/{}/mode/{}/update'.format(client.app_id, request_path_params_obj.resource_id, request_path_params_obj.sid, request_path_params_obj.mode)
    client.logger.debug("url:%s", url)

    return client.call_api('POST', url, post_json=utils.to_json(request_body_obj), response_type=response_type, response_obj=response_obj)
