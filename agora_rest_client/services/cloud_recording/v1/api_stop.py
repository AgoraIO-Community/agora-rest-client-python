from agora_rest_client.core import request
from agora_rest_client.core import response

"""
官方文档: https://doc.shengwang.cn/api-ref/cloud-recording/restful/cloud-recording/operations/post-v1-apps-appid-cloud_recording-resourceid-resourceid-sid-sid-mode-mode-stop
开始录制后, 你可以调用 stop 方法离开频道, 停止录制. 录制停止后如需再次录制, 必须再调用 acquire 方法请求一个新的 Resource ID.
对于每个声网账号, 每秒钟的请求数限制为 10 次. 如需提高此限制, 请联系技术支持.
stop 请求仅在会话内有效. 如果录制启动错误, 或录制已结束, 调用 stop 将返回 404.
非页面录制模式下, 当频道空闲(无用户)超过预设时间(默认为 30 秒) 后, 云端录制也会自动退出频道, 停止录制.
"""

class ClientRequest(request.RequestObject):
    """
    type: boolean

    设置 stop 方法的响应机制:
    true: 异步. 调用 stop 后立即收到响应.
    false: 同步. 调用 stop 后, 你需等待所有录制文件上传至第三方云存储方后会收到响应. 声网预期上传时间不超过 20 秒, 如果上传超时, 你会收到错误码 50.

    default: false
    """
    async_stop = None

class Payload(response.ResponseObject):
    """
    type: string

    当前录制上传的状态:
    "uploaded": 本次录制的文件已经全部上传至指定的第三方云存储.
    "backuped": 本次录制的文件已经全部上传完成, 但是至少有一个 TS 文件上传到了声网备份云. 声网服务器会自动将这部分文件继续上传至指定的第三方云存储.
    "unknown": 未知状态.

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.UploadingStatus`
    """
    uploadingStatus = None

class ExtensionServiceState(response.ResponseObject):
    """
    type: object

    页面录制模式下, 上传服务返回的字段

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_stop.Payload`
    """
    payload = None

    """
    type: string

    服务类型:
    "upload_service": 上传服务.
    "web_recorder_service": 页面录制服务.

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.ExtensionServiceStateName`
    """
    serviceName = None

class ServerResponse(response.ResponseObject):
    """
    type: array[object]

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_stop.ExtensionServiceState`
    """
    extensionServiceState = None

class RequestPathParamsApiStop(request.RequestObject):
    """
    type: required string

    录制模式:
    individual: 单流录制模式.
    mix: 合流录制模式.
    web: 页面录制模式.

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.Mode`
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

class RequestBodyApiStop(request.RequestObject):
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

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_stop.ClientRequest`
    """
    clientRequest = None

class ResponseApiStop(response.ResponseObject):
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

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_stop.ServerResponse`
    """
    serverResponse = None

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

def api_stop(client, request_path_params_obj, request_body_obj, response_obj=ResponseApiStop, trace_id=None):
    """
    Stop recording
    停止云端录制

    :type client: object
    :param client: CloudRecordingClient object

    :type request_path_params_obj: object
    :param request_path_params_obj: request path params object
    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_stop.RequestPathParamsApiStop`

    :type request_body_obj: object
    :param request_body_obj: request body object
    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_stop.RequestBodyApiStop`

    :type response_obj: object
    :param response_obj: response object
    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_stop.ResponseApiStop`

    :type trace_id: string
    :param trace_id: trace id

    :return: response object ResponseApiStop
    """
    url = '/v1/apps/{}/cloud_recording/resourceid/{}/sid/{}/mode/{}/stop'.format(client.app_id, request_path_params_obj.resource_id, request_path_params_obj.sid, request_path_params_obj.mode)
    client.logger.debug("url:%s", url)

    return client.call_api('POST', url, post_json=request_body_obj.to_dict(), response_obj=response_obj, trace_id=trace_id)
