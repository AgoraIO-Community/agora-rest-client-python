from agora_rest_client.core import request
from agora_rest_client.core import response

"""
官方文档: https://doc.shengwang.cn/api-ref/cloud-recording/restful/cloud-recording/operations/post-v1-apps-appid-cloud_recording-resourceid-resourceid-sid-sid-mode-mode-updateLayout
开始合流录制后, 你可以调用该方法(updateLayout)更新合流布局.
每次调用该方法都会覆盖原来的布局设置. 例如, 在开始录制时设置了 backgroundColor 为 "#FF0000"(红色), 如果调用 updateLayout 方法更新合流布局时如果不再设置 backgroundColor 字段, 背景色就会变为黑色(默认值).

对于每个声网账号, 每秒钟的请求数限制为 10 次. 如需提高此限制, 请联系技术支持.
updateLayout 请求仅在会话内有效. 如果录制启动错误, 或录制已结束, 调用 updateLayout 将返回 404.
如果需要连续调用 updateLayout 方法更新合流布局, 请在收到上一次 updateLayout 响应后再进行调用, 否则可能导致请求结果与预期不一致.
"""

class LayoutConfig(request.RequestObject):
    """
    type: string

    字符串内容为待显示在该区域的用户的 UID, 32 位无符号整数.
    如果不指定 UID, 会按照用户加入频道的顺序自动匹配 layoutConfig 中的画面设置.
    """
    uid = None

    """
    type: required number<float>

    屏幕里该画面左上角的横坐标的相对值, 精确到小数点后六位. 从左到右布局, 0.0 在最左端, 1.0 在最右端. 该字段也可以设置为整数 0 或 1.
    >= 0 <= 1
    """
    x_axis = None

    """
    type: required number<float>

    屏幕里该画面左上角的纵坐标的相对值, 精确到小数点后六位. 从上到下布局, 0.0 在最上端, 1.0 在最下端. 该字段也可以设置为整数 0 或 1.
    >= 0 <= 1
    """
    y_axis = None

    """
    type: required number<float>

    该画面宽度的相对值, 精确到小数点后六位. 该字段也可以设置为整数 0 或 1.
    >= 0 <= 1
    """
    width = None

    """
    type: required number<float>

    该画面高度的相对值, 精确到小数点后六位. 该字段也可以设置为整数 0 或 1.
    >= 0 <= 1
    """
    height = None

    """
    type: number<float>

    图像的透明度. 精确到小数点后六位. 0.0 表示图像为透明的, 1.0 表示图像为完全不透明的.
    >= 0 <= 1

    default: 1
    """
    alpha = None

    """
    type: number

    画面显示模式:
    0: 裁剪模式. 优先保证画面被填满. 视频尺寸等比缩放, 直至整个画面被视频填满. 如果视频长宽与显示窗口不同, 则视频流会按照画面设置的比例进行周边裁剪后填满画面.
    1: 缩放模式. 优先保证视频内容全部显示. 视频尺寸等比缩放, 直至视频窗口的一边与画面边框对齐. 如果视频尺寸与画面尺寸不一致, 在保持长宽比的前提下, 将视频进行缩放后填满画面, 缩放后的视频四周会有一圈黑边.

    default: 0

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.RenderMode`
    """
    render_mode = None

class BackgroundConfig(request.RequestObject):
    """
    type: required string

    字符串内容为用户 UID.
    """
    uid = None

    """
    type: required string

    该用户的背景图 URL. 配置背景图后, 当该⽤户停止发送视频流超过 3.5 秒, 画⾯将切换为该背景图.
    URL 支持 HTTP 和 HTTPS 协议, 图片格式支持 JPG 和 BMP. 图片大小不得超过 6 MB. 录制服务成功下载图片后, 设置才会生效; 如果下载失败, 则设置不⽣效. 不同字段设置可能会互相覆盖, 具体规则详见设置背景色或背景图.
    """
    image_url = None

    """
    type: number

    画面显示模式:
    0: 裁剪模式. 优先保证画面被填满. 视频尺寸等比缩放, 直至整个画面被视频填满. 如果视频长宽与显示窗口不同, 则视频流会按照画面设置的比例进行周边裁剪后填满画面.
    1: 缩放模式. 优先保证视频内容全部显示. 视频尺寸等比缩放, 直至视频窗口的一边与画面边框对齐. 如果视频尺寸与画面尺寸不一致, 在保持长宽比的前提下, 将视频进行缩放后填满画面, 缩放后的视频四周会有一圈黑边.

    default: 0

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.RenderMode`
    """
    render_mode = None

class ClientRequest(request.RequestObject):
    """
    type: string

    仅需在垂直布局下设置. 指定显示大视窗画面的用户 UID. 字符串内容的整型取值范围 1 到 (232-1), 且不可设置为 0.
    """
    maxResolutionUid = None

    """
    type: number

    视频合流布局:
    0: 悬浮布局. 第一个加入频道的用户在屏幕上会显示为大视窗, 铺满整个画布, 其他用户的视频画面会显示为小视窗, 从下到上水平排列, 最多 4 行, 每行 4 个画面, 最多支持共 17 个画面.
    1: 自适应布局. 根据用户的数量自动调整每个画面的大小, 每个用户的画面大小一致, 最多支持 17 个画面.
    2: 垂直布局. 指定 maxResolutionUid 在屏幕左侧显示大视窗画面, 其他用户的小视窗画面在右侧垂直排列, 最多两列, 一列 8 个画面, 最多支持共 17 个画面.
    3: 自定义布局. 由你在 layoutConfig 字段中自定义合流布局.

    default: 0

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.MixedVideoLayout`
    """
    mixedVideoLayout = None

    """
    type: string

    视频画布的背景颜色. 支持 RGB 颜色表, 字符串格式为 # 号和 6 个十六进制数. 默认值 "#000000", 代表黑色.

    default: #000000
    """
    backgroundColor = None

    """
    type: string

    视频画布的背景图的 URL. 背景图的显示模式为裁剪模式.
    裁剪模式: 优先保证画面被填满. 背景图尺寸等比缩放, 直至整个画面被背景图填满. 如果背景图长宽与显示窗口不同, 则背景图会按照画面设置的比例进行周边裁剪后填满画面.
    """
    backgroundImage = None

    """
    type: string

    默认的用户画面背景图的 URL.
    配置该字段后, 当任一⽤户停止发送视频流超过 3.5 秒, 画⾯将切换为该背景图; 如果针对某 UID 单独设置了背景图, 则该设置会被覆盖.
    """
    defaultUserBackgroundImage = None

    """
    type: array[object]

    用户的合流画面布局. 由每个用户对应的布局画面设置组成的数组, 支持最多 17 个用户.
    注意: 仅需在自定义布局下设置.

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_update_layout.LayoutConfig`
    """
    layoutConfig = None

    """
    type: array[object]

    用户的背景图设置.

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_update_layout.BackgroundConfig`
    """
    backgroundConfig = None

class RequestPathParamsApiUpdateLayout(request.RequestObject):
    """
    type: required string

    录制模式. 只支持 mix, 代表合流录制模式.

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

class RequestBodyApiUpdateLayout(request.RequestObject):
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

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_update_layout.ClientRequest`
    """
    clientRequest = None

class ResponseApiUpdateLayout(response.ResponseObject):
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

    录制 ID. 标识一次录制周期.
    """
    sid = None

def api_update_layout(client, request_path_params_obj, request_body_obj, response_obj=ResponseApiUpdateLayout, trace_id=None):
    """
    Update layout of the recording
    更新云端录制合流布局

    :type client: object
    :param client: CloudRecordingClient object

    :type request_path_params_obj: object
    :param request_path_params_obj: request path params object
    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_update_layout.RequestPathParamsApiUpdateLayout`

    :type request_body_obj: object
    :param request_body_obj: request body object
    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_update_layout.RequestBodyApiUpdateLayout`

    :type response_obj: object
    :param response_obj: response object
    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_update_layout.ResponseApiUpdateLayout`

    :type trace_id: string
    :param trace_id: trace id

    :return: response object ResponseApiUpdateLayout
    """
    url = '/v1/apps/{}/cloud_recording/resourceid/{}/sid/{}/mode/{}/updateLayout'.format(client.app_id, request_path_params_obj.resource_id, request_path_params_obj.sid, request_path_params_obj.mode)
    client.logger.debug("url:%s", url)

    return client.call_api('POST', url, post_json=request_body_obj.to_dict(), response_obj=response_obj, trace_id=trace_id)
