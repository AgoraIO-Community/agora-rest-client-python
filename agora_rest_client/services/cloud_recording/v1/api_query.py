from agora_rest_client.core import request
from agora_rest_client.core import response

"""
官方文档: https://doc.shengwang.cn/api-ref/cloud-recording/restful/cloud-recording/operations/get-v1-apps-appid-cloud_recording-resourceid-resourceid-sid-sid-mode-mode-query
开始录制后, 你可以调用 query 方法查询录制状态.
对于每个声网账号, 每秒钟的请求数限制为 10 次. 如需提高此限制, 请联系技术支持.
query 请求仅在会话内有效. 如果录制启动错误, 或录制已结束, 调用 query 将返回 404.
"""

class FileList(response.ResponseObject):
    """
    type: string

    录制产生的 M3U8 文件和 MP4 文件的文件名.
    """
    filename = None

    """
    type: number

    该文件的录制开始时间, Unix 时间戳, 单位为毫秒.
    """
    sliceStartTime = None

class Payload(response.ResponseObject):
    """
    type: array[object]

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_query.FileList`
    """
    fileList = None

    """
    type: boolean

    页面录制是否处于暂停状态:
    """
    onhold = None

    """
    type: string

    将订阅内容上传至扩展服务的状态:
    "init": 服务正在初始化.
    "inProgress": 服务启动完成, 正在进行中.
    "exit": 服务退出.

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.ExtensionServiceState`
    """
    state = None

class ExtensionServiceState(response.ResponseObject):
    """
    type: object

    页面录制时会返回如下字段

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_query.Payload`
    """
    payload = None

    """
    type: string

    扩展服务的名称:
    web_recorder_service: 代表扩展服务为页面录制.
    rtmp_publish_service: 代表扩展服务为转推页面录制到 CDN.

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.ExtensionServiceName`
    """
    serviceName = None

class ServerResponse(response.ResponseObject):
    """
    type: number

    当前云服务的状态:
    0: 没有开始云服务.
    1: 云服务初始化完成.
    2: 云服务组件开始启动.
    3: 云服务部分组件启动完成.
    4: 云服务所有组件启动完成.
    5: 云服务正在进行中.
    6: 云服务收到停止请求.
    7: 云服务所有组件均停止.
    8: 云服务已退出.
    20: 云服务异常退出.

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.ServiceStatus`
    """
    status = None

    """
    type: array[object]

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_query.ExtensionServiceState`
    """
    extensionServiceState = None

class RequestPathParamsApiQuery(request.RequestObject):
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

class ResponseApiQuery(response.ResponseObject):
    """
    type: string

    云端录制使用的 Resource ID.
    """
    resourceId = None

    """
    type: string

    录制 ID.
    """
    sid = None

    """
    type: object

    页面录制模式下会返回的字段.

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_query.ServerResponse`
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

def api_query(client, request_path_params_obj, response_obj=ResponseApiQuery, trace_id=None):
    """
    Query the recording status
    查询云端录制状态

    :type client: object
    :param client: CloudRecordingClient object

    :type request_path_params_obj: object
    :param request_path_params_obj: request path params object
    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_query.RequestPathParamsApiQuery`

    :type response_obj: object
    :param response_obj: response object
    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_query.ResponseApiQuery`

    :type trace_id: string
    :param trace_id: trace id

    :return: response object ResponseApiQuery
    """
    url = '/v1/apps/{}/cloud_recording/resourceid/{}/sid/{}/mode/{}/query'.format(client.app_id, request_path_params_obj.resource_id, request_path_params_obj.sid, request_path_params_obj.mode)
    client.logger.debug("url:%s", url)

    return client.call_api('GET', url, response_obj=response_obj, trace_id=trace_id)
