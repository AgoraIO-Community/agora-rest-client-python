from agora_rest_client.core import utils

"""
官方文档: https://doc.shengwang.cn/api-ref/cloud-recording/restful/cloud-recording/operations/post-v1-apps-appid-cloud_recording-resourceid-resourceid-sid-sid-mode-mode-update
开始录制后, 你可以调用 update 方法更新如下录制配置: 
对单流录制和合流录制, 更新订阅名单. 
对页面录制, 设置暂停/恢复页面录制, 或更新页面录制转推到 CDN 的推流地址(URL). 

对于每个声网账号, 每秒钟的请求数限制为 10 次. 如需提高此限制, 请联系技术支持. 
update 请求仅在会话内有效. 如果录制启动错误, 或录制已结束, 调用 update 将返回 404. 
如果需要连续调用 update 方法更新录制设置, 请在收到上一次 update 响应后再进行调用, 否则可能导致请求结果与预期不一致. 
"""

class AudioUidList(object):
    """
    type: array[string]

    指定订阅哪几个 UID 的音频流. 如需订阅全部 UID 的音频流, 则无需设置该字段. 数组长度不得超过 32, 不推荐使用空数组. 该字段和 unsubscribeAudioUids 只能设一个. 详见设置订阅名单. 

    注意: 
    该字段仅适用于 streamTypes 设为音频, 或音频和视频的情况. 
    如果你设置了音频的订阅名单, 但没有设置视频的订阅名单, 云端录制服务不会订阅任何视频流. 反之亦然. 
    设为 ["#allstream#"]` 可订阅频道内所有 UID 的音频流. 
    """
    subscribeAudioUids = []

    """
    type: array[string]

    指定不订阅哪几个 UID 的音频流. 云端录制会订阅频道内除指定 UID 外所有 UID 的音频流. 数组长度不得超过 32, 不推荐使用空数组. 该字段和 subscribeAudioUids 只能设一个. 详见设置订阅名单. 
    """
    unsubscribeAudioUids = []

class VideoUidList(object):
    """
    type: array[string]

    指定订阅哪几个 UID 的视频流. 如需订阅全部 UID 的视频流, 则无需设置该字段. 数组长度不得超过 32, 不推荐使用空数组. 该字段和 unsubscribeVideoUids 只能设一个. 详见设置订阅名单. 

    注意: 
    该字段仅适用于 streamTypes 设为视频, 或音频和视频的情况. 
    如果你设置了视频的订阅名单, 但没有设置音频的订阅名单, 云端录制服务不会订阅任何音频流. 反之亦然. 
    设为 ["#allstream#"] 可订阅频道内所有 UID 的视频流. 
    """
    subscribeVideoUids = []

    """
    type: array[string]

    指定不订阅哪几个 UID 的视频流. 云端录制会订阅频道内除指定 UID 外所有 UID 的视频流. 数组长度不得超过 32, 不推荐使用空数组. 该字段和 subscribeVideoUids 只能设一个. 详见设置订阅名单. 
    """
    unsunscribeVideoUids = []

class StreamSubscribe(object):
    """
    type: object

    音频订阅名单. 
    注意: 该字段仅适用于 streamTypes 设为音频, 或音频和视频的情况. 
    """
    audioUidList = AudioUidList()

    """
    type: object

    视频订阅名单. 
    注意: 该字段仅适用于 streamTypes 设为视频, 或音频和视频的情况. 
    """
    videoUidList = VideoUidList()

class WebRecordingConfig(object):
    """
    type: boolean

    是否在启动页面录制任务时暂停页面录制. 
    true: 在启动页面录制任务时暂停页面录制. 开启页面录制任务后立即暂停录制, 录制服务会打开并渲染待录制页面, 但不生成切片文件. 
    false: 启动页面录制任务并进行页面录制. 
    
    建议你按照如下流程使用 onhold 字段: 
    调用 start 方法时将 onhold 设为 true, 开启并暂停页面录制, 自行判断页面录制开始的合适时机. 
    调用 update 并将 onhold 设为 false, 继续进行页面录制. 如果需要连续调用 update 方法暂停或继续页面录制, 请在收到上一次 update 响应后再进行调用, 否则可能导致请求结果与预期不一致. 

    default: false
    """
    onhold = None

class Outputs(object):
    """
    type: string

    CDN 推流 URL. 

    注意: 
    URL 仅支持 RTMP 和 RTMPS 协议. 
    支持的最大转推 CDN 路数为 1. 
    """
    rtmpUrl = None

class RtmpPublishConfig(object):
    """
    type: array[object]
    """
    outputs = [Outputs()]

class ClientRequest(object):
    """
    type: object

    更新订阅名单. 
    注意: 仅需在单流录制和合流录制模式下设置. 
    """
    streamSubscribe = StreamSubscribe()

    """
    type: object

    用于更新页面录制配置项. 
    注意: 仅需在页面录制模式下设置. 
    """
    webRecordingConfig = WebRecordingConfig()

    """
    type: object

    用于更新转推页面录制到 CDN 的配置项. 
    注意: 仅需在页面录制模式下, 且转推页面录制到 CDN 时设置. 
    """
    rtmpPublishConfig = RtmpPublishConfig()

class RequestPathParamsApiUpdate(object):
    """
    type: required string

    录制模式: 
    individual: 单流录制模式. 
    mix: 合流录制模式. 
    web: 页面录制模式. 
    """
    mode = None

    """
    type: required string

    通过 acquire 请求获取到的 Resource ID. 
    """
    resource_id = None

    """
    type: required string

    通过 start 获取的录制 ID. 
    """
    sid = None

    def __init__(self, d):
        self.__dict__.update(d)

    def __str__(self):
        return ",".join(["{}={}".format(k, v) for k, v in self.__dict__.items()])

class RequestBodyApiUpdate(object):
    """
    type: required string

    录制服务所在频道的名称. 需要和你在 acquire 请求中输入的 cname 相同. 
    """
    cname = None

    """
    type: required string

    字符串内容为录制服务在 RTC 频道内使用的 UID, 用于标识该录制服务, 需要和你在 acquire 请求中输入的 uid 相同. 
    """
    uid = None

    """
    type: required object
    """
    clientRequest = ClientRequest()

    def __init__(self, d):
        self.__dict__.update(d)

    def __str__(self):
        return ",".join(["{}={}".format(k, v) for k, v in self.__dict__.items()])

class ResponseApiUpdate(object):
    """
    type: string

    录制的频道名. 
    """
    cname = None

    """
    type: string

    字符串内容为云端录制服务在 RTC 频道内使用的 UID, 用于标识频道内的录制服务. 
    """
    uid = None

    """
    type: string

    云端录制使用的 Resource ID. 
    """
    resourceId = None

    """
    type: string

    录制 ID. 标识每次录制周期. 
    """
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
    :param response_type: response type, `agora_rest_client.core.response.ResponseType`
    :param response_obj: response object
    :return: response object ResponseApiUpdate
    """
    url = '/v1/apps/{}/cloud_recording/resourceid/{}/sid/{}/mode/{}/update'.format(client.app_id, request_path_params_obj.resource_id, request_path_params_obj.sid, request_path_params_obj.mode)
    client.logger.debug("url:%s", url)

    return client.call_api('POST', url, post_json=utils.to_json(request_body_obj), response_type=response_type, response_obj=response_obj)
