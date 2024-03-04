from agora_rest_client.core import request
from agora_rest_client.core import response

"""
官方文档: https://doc.shengwang.cn/api-ref/cloud-recording/restful/cloud-recording/operations/post-v1-apps-appid-cloud_recording-resourceid-resourceid-mode-mode-start
通过 acquire 方法获取云端录制资源后, 调用 start 方法开始云端录制.
发起 start 请求后, 你还需要依据最佳实践检查录制服务是否已经成功启动.
对于每个声网账号, 每秒钟的请求数限制为 10 次. 如需提高此限制, 请联系技术支持
"""

class ExtensionParams(request.RequestObject):
    """
    type: required string

    加密模式. 设置该字段后, 第三方云存储服务会按照该加密模式将已上传的录制文件进行加密. 该字段仅适用于 Amazon S3
    kms: KMS 加密.
    aes256: AES256 加密.

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.AmazonS3Sse`
    """
    sse = None

    """
    type: required string

    标签内容. 设置该字段后, 第三方云存储服务会按照该标签内容将已上传的录制文件进行打标签操作. 该字段仅适用于阿里云和 Amazon S3
    """
    tag = None

class StorageConfig(request.RequestObject):
    """
    type: required number

    第三方云存储指定的地区信息.
    注意: 为确保录制文件上传的成功率和实时性, 第三方云存储的 region 与你发起请求的应用服务器必须在同一个区域中. 例如: 你发起请求的 App 服务器在中国大陆地区, 则第三方云存储需要设置为中国大陆区域内
    """
    region = None

    """
    type: required number

    第三方云存储平台.
    1: Amazon S3
    2: 阿里云
    3: 腾讯云
    5: Microsoft Azure
    6: 谷歌云
    7: 华为云
    8: 百度智能云

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.StorageVendor`
    """
    vendor = None

    """
    type: required string

    第三方云存储的 Bucket. Bucket 名称需要符合对应第三方云存储服务的命名规则.
    """
    bucket = None

    """
    type: required string

    第三方云存储的 Access Key(访问密钥). 如需延时转码, 则访问密钥必须具备读写权限; 否则建议只需提供写权限.
    """
    accessKey = None

    """
    type: required string

    第三方云存储的 Secret Key.
    """
    secretKey = None

    """
    type: array[string]

    录制文件在第三方云存储中的存储位置, 与录制文件名前缀有关. 如果设为 ["directory1","directory2"], 那么录制文件名前缀为 "directory1/directory2/", 即录制文件名为 directory1/directory2/xxx.m3u8. 前缀长度(包括斜杠)不得超过 128 个字符. 字符串中不得出现斜杠/下划线/括号等符号字符. 以下为支持的字符集范围:
    26 个小写英文字母 a~z
    26 个大写英文字母 A~Z
    10 个数字 0-9
    """
    fileNamePrefix = None

    """
    type: object

    第三方云存储服务会按照该字段设置对已上传的录制文件进行加密和打标签.

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.ExtensionParams`
    """
    extensionParams = None

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

class TranscodingConfig(request.RequestObject):
    """
    type: required number

    视频的宽度, 单位为像素. width 和 height 的乘积不能超过 1920 × 1080.
    <= 1920

    default: 360
    """
    width = None

    """
    type: required number

    视频的高度, 单位为像素. width 和 height 的乘积不能超过 1920 × 1080.
    <= 1920

    default: 640
    """
    height = None

    """
    type: required number

    视频的帧率, 单位 fps.

    default: 15
    """
    fps = None

    """
    type: required number

    视频的码率, 单位 Kbps.

    default: 500
    """
    bitrate = None

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

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.LayoutConfig`
    """
    layoutConfig = None

    """
    type: array[object]

    用户的背景图设置.

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.BackgroundConfig`
    """
    backgroundConfig = None

class RecordingConfig(request.RequestObject):
    """
    type: required number

    频道场景.
    0: 通信场景.
    1: 直播场景.
    频道场景必须与声网 RTC SDK 的设置一致, 否则可能导致问题.

    default: 0

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.ChannelType`
    """
    channelType = None

    """
    type: number

    解密模式. 如果你在 SDK 客户端设置了频道加密, 那么你需要对云端录制服务设置与加密相同的解密模式.
    0: 不加密.
    1: AES_128_XTS 加密模式. 128 位 AES 加密, XTS 模式.
    2: AES_128_ECB 加密模式. 128 位 AES 加密, ECB 模式.
    3: AES_256_XTS 加密模式. 256 位 AES 加密, XTS 模式.
    4: SM4_128_ECB 加密模式. 128 位 SM4 加密, ECB 模式.
    5: AES_128_GCM 加密模式. 128 位 AES 加密, GCM 模式.
    6: AES_256_GCM 加密模式. 256 位 AES 加密, GCM 模式.
    7: AES_128_GCM2 加密模式. 128 位 AES 加密, GCM 模式. 相比于 AES_128_GCM 加密模式, AES_128_GCM2 加密模式安全性更高且需要设置密钥和盐.
    8: AES_256_GCM2 加密模式. 256 位 AES 加密, GCM 模式. 相比于 AES_256_GCM 加密模式, AES_256_GCM2 加密模式安全性更高且需要设置密钥和盐.

    default: 0

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.DecryptionMode`
    """
    decryptionMode = None

    """
    type: string

    与加解密相关的密钥. 仅需在 decryptionMode 非 0 时设置.
    """
    secret = None

    """
    type: string

    与加解密相关的盐. Base64 编码/32 位字节. 仅需在 decryptionMode 为 7 或 8 时设置.
    """
    salt = None

    """
    type: number

    最大频道空闲时间. 单位为秒. 最大值不超过 30 天. 超出最大频道空闲时间后, 录制服务会自动退出. 录制服务退出后, 如果你再次发起 start 请求, 会产生新的录制文件.
    频道空闲: 直播频道内无任何主播, 或通信频道内无任何用户.
    >= 5 <= 2592000

    default: 30
    """
    maxIdleTime = None

    """
    type: number

    订阅的媒体流类型.
    0: 仅订阅音频. 适用于智能语音审核场景.
    1: 仅订阅视频.
    2: 订阅音频和视频.

    default: 2

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.StreamTypes`
    """
    streamTypes = None

    """
    type: number

    设置订阅的视频流类型. 如果你在 SDK 客户端开启了双流模式, 你可以选择订阅视频大流或者小流.
    0: 视频大流, 即高分辨率高码率的视频流
    1: 视频小流, 即低分辨率低码率的视频流

    default: 0

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.VideoStreamType`
    """
    videoStreamType = None

    """
    type: array[string]

    指定订阅哪几个 UID 的音频流. 如需订阅全部 UID 的音频流, 则无需设置该字段. 数组长度不得超过 32, 不推荐使用空数组. 该字段和 unsubscribeAudioUids 只能设一个. 详见设置订阅名单.
    注意:
    该字段仅适用于 streamTypes 设为音频, 或音频和视频的情况.
    如果你设置了音频的订阅名单, 但没有设置视频的订阅名单, 云端录制服务不会订阅任何视频流. 反之亦然.
    设为 ["#allstream#"]` 可订阅频道内所有 UID 的音频流.
    """
    subscribeAudioUids = None

    """
    type: array[string]

    指定不订阅哪几个 UID 的音频流. 云端录制会订阅频道内除指定 UID 外所有 UID 的音频流. 数组长度不得超过 32, 不推荐使用空数组. 该字段和 subscribeAudioUids 只能设一个. 详见设置订阅名单.
    """
    unsubscribeAudioUids = None

    """
    type: array[string]

    指定订阅哪几个 UID 的视频流. 如需订阅全部 UID 的视频流, 则无需设置该字段. 数组长度不得超过 32, 不推荐使用空数组. 该字段和 unsubscribeVideoUids 只能设一个. 详见设置订阅名单.
    注意:
    该字段仅适用于 streamTypes 设为视频, 或音频和视频的情况.
    如果你设置了视频的订阅名单, 但没有设置音频的订阅名单, 云端录制服务不会订阅任何音频流. 反之亦然.
    设为 ["#allstream#"] 可订阅频道内所有 UID 的视频流.
    """
    subscribeVideoUids = None

    """
    type: array[string]

    指定不订阅哪几个 UID 的视频流. 云端录制会订阅频道内除指定 UID 外所有 UID 的视频流. 数组长度不得超过 32, 不推荐使用空数组. 该字段和 subscribeVideoUids 只能设一个. 详见设置订阅名单.
    """
    unsubscribeVideoUids = None

    """
    type: number

    预估的订阅人数峰值.
    0: 1 到 2 个 UID.
    1: 3 到 7 个 UID.
    2: 8 到 12 个 UID.
    3: 13 到 17 个 UID.
    4: 17 到 32 个 UID.
    5: 32 到 49 个 UID.

    注意:
    仅需在单流录制模式下设置, 且单流录制模式下必填.
    举例来说, 如果 subscribeVideoUids 为 ["100","101","102"], subscribeAudioUids 为 ["101","102","103"], 则订阅人数为 4 人.

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.SubscribeUidGroup`
    """
    subscribeUidGroup = None

    """
    type: string

    媒体流的输出模式. 详见媒体流输出模式.
    "default": 默认模式. 录制过程中音频转码, 分别生成 M3U8 音频索引文件和视频索引文件.
    "standard": 标准模式. 声网推荐使用该模式. 录制过程中音频转码, 分别生成 M3U8 音频索引文件/视频索引文件和合并的音视频索引文件. 如果在 Web 端使用 VP8 编码, 则生成一个合并的 MPD 音视频索引文件.
    "original": 原始编码模式. 适用于单流音频不转码录制. 仅订阅音频时(streamTypes 为 0)时该字段生效, 录制过程中音频不转码, 生成 M3U8 音频索引文件.

    注意: 仅需在单流录制模式下设置.

    default: default

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.StreamMode`
    """
    streamMode = None

    """
    type: number

    设置输出音频的采样率/码率/编码模式和声道数.
    0: 48 kHz 采样率, 音乐编码, 单声道, 编码码率约 48 Kbps.
    1: 48 kHz 采样率, 音乐编码, 单声道, 编码码率约 128 Kbps.
    2: 48 kHz 采样率, 音乐编码, 双声道, 编码码率约 192 Kbps.

    注意: 仅需在合流录制模式下设置.

    default: 0

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.AudioProfile`
    """
    audioProfile = None

    """
    type: object

    转码输出的视频配置项. 取值可参考设置录制输出视频的分辨率.

    注意: 仅需在单流录制和合流录制模式下设置.

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.TranscodingConfig`
    """
    transcodingConfig = None

class RecordingFileConfig(request.RequestObject):
    """
    type: array[string]

    录制生成的视频文件类型:
    "hls": 默认值. M3U8 和 TS 文件.
    "mp4": MP4 文件.

    注意:
    单流录制模式下, 且非仅截图情况, 使用默认值即可.
    合流录制和页面录制模式下, 你需设为 ["hls","mp4"]. 仅设为 ["mp4"] 会收到报错. 设置后, 录制文件行为如下:
        合流录制模式: 录制服务会在当前 MP4 文件时长超过约 2 小时或文件大小超过约 2 GB 左右时, 创建一个新的 MP4 文件.
        页面录制模式: 录制服务会在当前 MP4 文件时长超过 maxVideoDuration 时, 创建一个新的 MP4 文件.

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.AvFileType`
    """
    avFileType = None

class SnapshotConfig(request.RequestObject):
    """
    type: number

    云端录制定期截图的截图周期. 单位为秒.
    >= 5 <= 3600

    default: 10
    """
    captureInterval = None

    """
    type: required array[string]

    截图的文件格式. 目前只支持 ["jpg"], 即生成 JPG 格式的截图文件.

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.SnapshotFileType`
    """
    fileType = None

class ServiceParam(request.RequestObject):
    """
    type: required string

    待录制页面的地址.
    """
    url = None

    """
    type: required number

    输出音频的采样率/码率/编码模式和声道数.
    0: 48 kHz 采样率, 音乐编码, 单声道, 编码码率约 48 Kbps.
    1: 48 kHz 采样率, 音乐编码, 单声道, 编码码率约 128 Kbps.
    2: 48 kHz 采样率, 音乐编码, 双声道, 编码码率约 192 Kbps.

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.AudioProfile`
    """
    audioProfile = None

    """
    type: required number

    输出视频的宽度, 单位为 pixel. videoWidth 和 videoHeight 的乘积需小于等于 1920 × 1080. 推荐值可参考如何设置页面录制移动端网页模式的输出视频分辨率.
    >= 240 <= 1920
    """
    videoWidth = None

    """
    type: required number

    输出视频的高度, 单位为 pixel. videoWidth 和 videoHeight 的乘积需小于等于 1920 × 1080. 推荐值可参考如何设置页面录制移动端网页模式的输出视频分辨率.
    >= 240 <= 1920
    """
    videoHeight = None

    """
    type: required number

    页面录制的最大时长, 单位为小时. 超出该值后页面录制会自动停止.
    建议取值不超过你在 acquire 方法中设置的 resourceExpiredHour 的值.
    计费相关: 页面录制停止前会持续计费, 因此请根据实际业务情况设置合理的值或主动停止页面录制.
    >= 1 <= 720
    """
    maxRecordingHour = None

    """
    type: number

    输出视频的码率, 单位为 Kbps. 针对不同的输出视频分辨率, videoBitrate 的默认值不同:
    输出视频分辨率大于或等于 1280 × 720: 默认值为 2000.
    输出视频分辨率小于 1280 × 720: 默认值为 1500.
    """
    videoBitrate = None

    """
    type: number

    输出视频的帧率, 单位为 fps.
    >= 5 <= 60

    default: 15
    """
    videoFps = None

    """
    type: boolean

    是否开启移动端网页模式:
    true: 开启. 开启后, 录制服务使用移动端网页渲染模式录制当前页面.
    false: (默认)不开启.

    default: false
    """
    mobile = None

    """
    type: number

    页面录制生成的 MP4 切片文件的最大时长, 单位为分钟. 页面录制过程中, 录制服务会在当前 MP4 文件时长超过约 maxVideoDuration 左右时创建一个新的 MP4 切片文件.
    >= 30 <= 240

    default: 120
    """
    maxVideoDuration = None

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

    """
    type: number

    设置页面加载超时时间, 单位为秒. 详见页面加载超时检测.
    0 或不设置, 表示不检测页面加载状态.
    [1,60] 之间的整数, 表示页面加载超时时间.
    >= 0 <= 60

    default: 0
    """
    readyTimeout = None

class ExtensionServices(request.RequestObject):
    """
    type: required string

    扩展服务的名称:
    web_recorder_service: 代表扩展服务为页面录制.
    rtmp_publish_service: 代表扩展服务为转推页面录制到 CDN.

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.ExtensionServiceName`
    """
    serviceName = None

    """
    type: string

    扩展服务内的错误处理策略:
    "error_abort": 页面录制时默认且只能为该值. 表示当前扩展服务出错时, 停止其他扩展服务.
    "error_ignore": 转推页面录制到 CDN 时默认且只能为该值. 表示当前扩展服务出错时, 其他扩展服务不受影响.

    如果页面录制服务或录制上传服务异常, 那么推流到 CDN 失败, 因此页面录制服务出错会影响转推页面录制到 CDN 服务.
    转推到 CDN 的过程发生异常时, 页面录制不受影响.

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.ExtensionErrorHandlePolicy`
    """
    errorHandlePolicy = None

    """
    type: required object

    页面录制时需设置如下字段

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.ServiceParam`
    """
    serviceParam = None

class ExtensionServiceConfig(request.RequestObject):
    """
    type: string

    错误处理策略. 默认且仅可设为 "error_abort", 表示当扩展服务发生错误后, 订阅和云端录制的其他非扩展服务都停止.

    default: error_abort

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.ExtensionErrorHandlePolicy`
    """
    errorHandlePolicy = None

    """
    type: required array[object]

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.ExtensionServices`
    """
    extensionServices = None

class AppsCollection(request.RequestObject):
    """
    type: string

    各云端录制应用的组合方式.
    postpone_transcoding: 如需延时转码或延时混音, 则选用此种方式.
    default: 除延时转码和延时混音外, 均选用此种方式.

    default: default

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.CombinationPolicy`
    """
    combinationPolicy = None

class TransConfig(request.RequestObject):
    """
    type: required string

    模式:
    "postponeTranscoding": 延时转码.
    "audioMix": 延时混音.

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.PostponeTranscodeMode`
    """
    transMode = None

class Container(request.RequestObject):
    """
    type: string

    文件的容器格式, 支持如下取值:
    "mp4": 延时转码时的默认格式. MP4 格式.
    "mp3": 延时混音时的默认格式. MP3 格式.
    "m4a": M4A 格式.
    "aac": AAC 格式.

    注意: 延时转码暂时只能设为 MP4 格式.

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.ContainerFormat`
    """
    format = None

class Audio(request.RequestObject):
    """
    type: string

    音频采样率 (Hz), 支持如下取值:
    "48000": 48 kHz.
    "32000": 32 kHz.
    "16000": 16 kHz.

    default: 48000

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.AudioSampleRate`
    """
    sampleRate = None

    """
    type: string

    音频码率 (Kbps), 支持取值且默认取值为 "48000".

    default: 48000
    """
    bitrate = None

    """
    type: string

    音频声道数, 支持如下取值:
    "1": 单声道.
    "2": 双声道.

    default: 2

    :value: enum of `agora_rest_client.services.cloud_recording.v1.api.AudioChannels`
    """
    channels = None

class TranscodeOptions(request.RequestObject):
    """
    type: required object

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.TransConfig`
    """
    transConfig = None

    """
    type: object

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.Container`
    """
    container = None

    """
    type: object

    文件的音频属性.

    注意: 仅需在单流录制模式下, 且开启延时混音时设置.

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.Audio`
    """
    audio = Audio()

class ClientRequest(request.RequestObject):
    """
    type: string

    用于鉴权的动态密钥(Token). 如果你的项目已启用 App 证书, 则务必在该字段中传入你项目的动态密钥. 详见使用 Token 鉴权.
    注意:
    仅需在单流录制和合流录制模式下设置.
    云端录制服务暂不支持更新 Token. 为保证录制正常, 请确保 Token 有效时长大于你预计的录制时长, 以避免 Token 过期导致录制任务退出频道而结束录制.
    """
    token = None

    """
    type: required object

    第三方云存储的配置项.

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.StorageConfig`
    """
    storageConfig = None

    """
    type: object

    录制的音视频流配置项.
    注意: 仅需在单流录制和合流录制模式下设置.

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.RecordingConfig`
    """
    recordingConfig = None

    """
    type: object

    录制文件配置项.
    注意: 仅截图时不可设置该字段, 其他情况都需要设置该字段. 其他情况包含如下:
    单流录制模式下, 不转码录制, 转码录制, 或同时录制和截图.
    合流录制.
    页面录制模式下, 仅页面录制, 或同时页面录制和转推到 CDN.

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.RecordingFileConfig`
    """
    recordingFileConfig = None

    """
    type: object

    视频截图配置项.
    注意: 仅需在单流录制模式下, 且使用截图功能时设置.
    截图使用须知:
    截图功能仅适用于单流录制模式(individual).
    你可以在一个单流录制进程中仅截图, 或同时录制和截图, 详见视频截图. 同时录制和截图的情况需要设置 recordingFileConfig 字段.
    如果录制服务或录制上传服务异常, 则截图失败. 截图异常时, 录制不受影响.
    使用截图时, streamTypes 必须设置为 1 或 2. 如果设置了 subscribeAudioUid, 则必须同时设置 subscribeVideoUids.

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.SnapshotConfig`
    """
    snapshotConfig = None

    """
    type: object

    扩展服务配置项.
    注意: 仅需在页面录制模式下设置.

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.ExtensionServiceConfig`
    """
    extensionServiceConfig = None

    """
    type: object

    应用配置项.
    注意: 仅需在单流录制模式下, 且开启延时转码或延时混音时设置.

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.AppsCollection`
    """
    appsCollection = None

    """
    type: object

    延时转码或延时混音下, 生成的录制文件的配置项.
    注意: 仅需在单流录制模式下, 且开启延时转码或延时混音时设置.

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.TranscodeOptions`
    """
    transcodeOptions = None

class RequestPathParamsApiStart(request.RequestObject):
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

class RequestBodyApiStart(request.RequestObject):
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

    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest`
    """
    clientRequest = None

class ResponseApiStart(response.RequestObject):
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

    """
    type: string

    录制 ID. 成功开始云端录制后, 你会得到一个 Sid (录制 ID). 该 ID 是一次录制周期的唯一标识.
    """
    sid = None

    """
    type: number

    状态码
    """
    code = None

def api_start(client, request_path_params_obj, request_body_obj, response_obj=ResponseApiStart, trace_id=None):
    """
    Start recording
    开始云端录制

    :type client: object
    :param client: CloudRecordingClient object

    :type request_path_params_obj: object
    :param request_path_params_obj: request path params object
    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.RequestPathParamsApiStart`

    :type request_body_obj: object
    :param request_body_obj: request body object
    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.RequestBodyApiStart`

    :type response_obj: object
    :param response_obj: response object
    :value: instance of `agora_rest_client.services.cloud_recording.v1.api_start.ResponseApiStart`

    :type trace_id: string
    :param trace_id: trace id

    :return: response object ResponseApiStart
    """
    url = '/v1/apps/{}/cloud_recording/resourceid/{}/mode/{}/start'.format(client.app_id, request_path_params_obj.resource_id, request_path_params_obj.mode)
    client.logger.debug("url:%s", url)

    return client.call_api('POST', url, post_json=request_body_obj.to_dict(), response_obj=response_obj, trace_id=trace_id, is_retry=True)
