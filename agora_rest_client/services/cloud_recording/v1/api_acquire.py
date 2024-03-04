from agora_rest_client.core import request
from agora_rest_client.core import response

"""
官方文档: https://doc.shengwang.cn/api-ref/cloud-recording/restful/cloud-recording/operations/post-v1-apps-appid-cloud_recording-acquire
在开始云端录制之前, 你需要调用 acquire 方法获取一个 Resource ID. 一个 Resource ID 只能用于一次云端录制服务.
为确保成功开始云端录制, 请在每次 acquire 请求获取到 Resource ID 后的 2 秒内立即发起对应的 start 请求.
批量获取 Resource ID 后进行批量 start 请求可能导致请求失败. acquire 和 start 的请求需配对调用. Resource ID 在获取到的 5 分钟内有效, 需尽快使用.
对于每个声网账号，每秒钟的请求数限制为 10 次。如需提高此限制，请联系技术支持
"""

class ClientRequest(request.RequestObject):
    """
    type: number

    云端录制资源使用场景:
    0: 实时音视频录制.
    1: 页面录制.
    2: 单流录制模式, 且开启延时转码或延时混音.
        延时转码: 录制服务会在录制后 24 小时内(特殊情况下会到 48 小时以上)对录制文件进行转码生成 MP4 文件, 并将 MP4 文件上传至你指定的第三方云存储. 该场景仅适用于单流录制模式.
        延时混音: 录制服务会在录制结束后 24 小时内(特殊情况下会到 48 小时以上)将指定频道内所有 UID 的录制文件合并并转码生成一个 MP3/M4A/AAC 文件, 并将文件上传至你指定的第三方云存储. 该场景仅适用于音频单流不转码录制模式.
        scene 设为 2 时, 你需要同时在 start 方法中设置 appsCollection 字段.
        在延时转码和延时混音的场景下, 录制文件会在声网边缘服务器上缓存, 最长不超过 24 小时. 如果你的业务对信息安全敏感, 为了确保数据合规, 请慎重考虑是否使用延时转码和延时混音功能. 如有任何疑虑, 请联系声网技术支持.
        在延时转码和延时混音的场景中, 声网建议你不要填写 region 字段, 也不要将其留空. 否则, 由于声网边缘服务器的动态调整和延时场景下录制文件缓存带来的数据合规风险, 声网录制服务将无法正常使用.

    default: 0

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.Scene`
    """
    scene = None

    """
    type: number

    云端录制 RESTful API 的调用时效. 从成功开启云端录制并获得 sid (录制 ID)后开始计算. 单位为小时.
    注意: 超时后, 你将无法调用 query, update, updateLayout 和 stop 方法.
    >= 1 <= 720

    default: 72
    """
    resourceExpiredHour = None

    """
    type: array[string]

    另一路或几路录制任务的 resourceId. 该字段用于排除指定的录制资源, 以便新发起的录制任务可以使用新区域的资源, 实现跨区域多路录制
    """
    excludeResourceIds = None

    """
    type: number

    指定使用某个区域的资源进行录制. 支持取值如下:
    0: 根据发起请求的区域就近调用资源.
    1: 中国.
    2: 东南亚.
    3: 欧洲.
    4: 北美.
    注意: 为加速录制文件上传, 当你使用的云存储区域和你发起请求的区域不同时, 建议你将该字段设为云存储区域.

    default: 0

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.RegionAffinity`
    """
    regionAffinity = None

class RequestBodyApiAcquire(request.RequestObject):
    """
    type: required string

    频道名:
    对于单流录制和合流录制模式, 该字段用于设置待录制的频道名.
    对于页面录制模式, 该字段用于区分录制进程. 字符串长度不得超过 128 字节.
    注意: 通过 appid/cname 和 uid 可以定位一个唯一的录制实例. 因此, 如果你想针对同一个频道进行多次录制, 可以使用相同的 appId 和 cname, 以及不同的 uid 来进行管理和区分.
    """
    cname = None

    """
    type: required string

    字符串内容为云端录制服务在频道内使用的 UID, 用于标识频道内的录制服务, 例如 "527841". 字符串内容需满足以下条件:
    取值范围 1 到 (232-1), 不可设置为 0.
    不能与当前频道内的任何 UID 重复.
    字段引号内为整型 UID, 且频道内所有用户均使用整型 UID.
    """
    uid = None

    """
    type: object

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_acquire.ClientRequest`
    """
    clientRequest = None

class ResponseApiAcquire(response.ResponseObject):
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

    云端录制资源 Resource ID. 使用这个 Resource ID 可以开始一段云端录制. 这个 Resource ID 的有效期为 5 分钟, 超时需要重新请求.
    """
    resourceId = None

def api_acquire(client, request_body_obj, response_obj=ResponseApiAcquire, trace_id=None):
    """
    Acquire a resource id
    获取云端录制资源

    :type client: object
    :param client: CloudRecordingClient object

    :type request_body_obj: object
    :param request_body_obj: request body object
    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_acquire.RequestBodyApiAcquire`

    :type response_obj: object
    :param response_obj: response object
    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_acquire.ResponseApiAcquire`

    :type trace_id: string
    :param trace_id: trace id

    :return: response object ResponseApiAcquire
    """
    url = '/v1/apps/{}/cloud_recording/acquire'.format(client.app_id)
    client.logger.debug("url:%s", url)

    return client.call_api('POST', url, post_json=request_body_obj.to_dict(), response_obj=response_obj, trace_id=trace_id)
