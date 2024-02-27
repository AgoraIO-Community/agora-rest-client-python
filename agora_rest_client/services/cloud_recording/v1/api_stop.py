from agora_rest_client.core import utils

"""
官方文档: https://doc.shengwang.cn/api-ref/cloud-recording/restful/cloud-recording/operations/post-v1-apps-appid-cloud_recording-resourceid-resourceid-sid-sid-mode-mode-stop
开始录制后, 你可以调用 stop 方法离开频道, 停止录制. 录制停止后如需再次录制, 必须再调用 acquire 方法请求一个新的 Resource ID. 
对于每个声网账号, 每秒钟的请求数限制为 10 次. 如需提高此限制, 请联系技术支持. 
stop 请求仅在会话内有效. 如果录制启动错误, 或录制已结束, 调用 stop 将返回 404. 
非页面录制模式下, 当频道空闲(无用户)超过预设时间(默认为 30 秒) 后, 云端录制也会自动退出频道, 停止录制. 
"""

class ClientRequest(object):
    """
    type: boolean

    设置 stop 方法的响应机制: 
    true: 异步. 调用 stop 后立即收到响应. 
    false: 同步. 调用 stop 后, 你需等待所有录制文件上传至第三方云存储方后会收到响应. 声网预期上传时间不超过 20 秒, 如果上传超时, 你会收到错误码 50. 

    default: false
    """
    async_stop = None

class Payload(object):
    """
    type: string

    当前录制上传的状态: 
    "uploaded": 本次录制的文件已经全部上传至指定的第三方云存储. 
    "backuped": 本次录制的文件已经全部上传完成, 但是至少有一个 TS 文件上传到了声网备份云. 声网服务器会自动将这部分文件继续上传至指定的第三方云存储. 
    "unknow": 未知状态. 
    """
    uploadingStatus = None
    
class ExtensionServiceState(object):
    """
    type: object

    页面录制模式下, 上传服务返回的字段
    """
    payload = Payload()

    """
    type: string

    服务类型: 
    "upload_service": 上传服务. 
    "web_recorder_service": 页面录制服务. 
    """
    serviceName = None

class ServerResponse(object):
    """
    type: array[object]
    """
    extensionServiceState = [ExtensionServiceState()]

class RequestPathParamsApiStop(object):
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

class RequestBodyApiStop(object):
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
    type: request object
    """
    clientRequest = ClientRequest()

    def __init__(self, d):
        self.__dict__.update(d)

    def __str__(self):
        return ",".join(["{}={}".format(k, v) for k, v in self.__dict__.items()])

class ResponseApiStop(object):
    """
    type: string

    云端录制使用的 Resource ID. 
    """
    resourceId = None

    """
    type: string

    录制 ID. 标识一次录制周期. 
    """
    sid = None

    """
    type: object

    页面录制场景下会返回的字段
    """
    serverResponse = ServerResponse()
    
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

    def __init__(self, d):
        self.__dict__.update(d)

    def __str__(self):
        return ",".join(["{}={}".format(k, v) for k, v in self.__dict__.items()])

def api_stop(client, request_path_params_obj, request_body_obj, response_type, response_obj=ResponseApiStop):
    """
    Stop recording

    :param client: CloudRecordingClient object
    :param request_path_params_obj: request object RequestPathParamsApiStop
    :param request_body_obj: request object RequestBodyApiStop
    :param response_type: response type, `agora_rest_client.core.response.ResponseType`
    :param response_obj: response object
    :return: response object ResponseApiStop
    """
    url = '/v1/apps/{}/cloud_recording/resourceid/{}/sid/{}/mode/{}/stop'.format(client.app_id, request_path_params_obj.resource_id, request_path_params_obj.sid, request_path_params_obj.mode)
    client.logger.debug("url:%s", url)

    return client.call_api('POST', url, post_json=utils.to_json(request_body_obj), response_type=response_type, response_obj=response_obj)
