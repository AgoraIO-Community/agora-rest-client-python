from enum import Enum

# Amazon S3 加密模式, Server-Side Encryption
class AmazonS3Sse(Enum):
    # KMS 加密
    KMS = 'kms'
    # AES256 加密
    AES_256 = 'aes256'

# 音频声道数
class AudioChannels(Enum):
    # 单声道
    MONO = '1'
    # 双声道
    STEREO = '2'

# 音频采样率
class AudioSampleRate(Enum):
    # 48 kHz
    SAMPLE_RATE_48 = '48000'
    # 32 kHz
    SAMPLE_RATE_32 = '32000'
    # 16 kHz
    SAMPLE_RATE_16 = '16000'

# 输出音频的采样率/码率/编码模式和声道数
class AudioProfile(Enum):
    # 48 kHz 采样率, 音乐编码, 单声道, 编码码率约 48 Kbps
    SAMPLE_RATE_48_MONO_ENCODING_48 = 0
    # 48 kHz 采样率, 音乐编码, 单声道, 编码码率约 128 Kbps
    SAMPLE_RATE_48_MONO_ENCODING_128 = 1
    # 48 kHz 采样率, 音乐编码, 双声道, 编码码率约 192 Kbps
    SAMPLE_RATE_48_STEREO_ENCODING_192 = 2

# 视频文件类型
class AvFileType(Enum):
    HLS = 'hls'
    MP4 = 'mp4'

# 频道场景
class ChannelType(Enum):
    # 通信场景
    COMMUNICATION = 0
    # 直播场景
    LIVE = 1

# 各云端录制应用的组合方式
class CombinationPolicy(Enum):
    # 如需延时转码或延时混音, 则选用此种方式
    POSTPONE_TRANSCODING = 'postpone_transcoding'
    # 除延时转码和延时混音外, 均选用此种方式
    DEFAULT = 'default'

# 文件的容器格式
class ContainerFormat(Enum):
    # 延时转码时的默认格式
    MP4 = 'mp4'
    # 延时混音时的默认格式
    MP3 = 'mp3'
    # M4A 格式
    M4A = 'm4a'
    # AAC 格式
    AAC= 'aac'

# 解密模式
class DecryptionMode(Enum):
    # 不加密
    NO_ENCRYPTION = 0
    # AES_128_XTS 加密模式
    AES_128_XTS = 1
    # AES_128_ECB 加密模式
    AES_128_ECB = 2
    # AES_256_XTS 加密模式
    AES_256_XTS = 3
    # SM4_128_ECB 加密模式
    SM4_128_ECB = 4
    # AES_128_GCM 加密模式
    AES_128_GCM = 5
    # AES_256_GCM 加密模式
    AES_256_GCM = 6
    # AES_128_GCM2 加密模式
    AES_128_GCM2 = 7
    # AES_256_GCM2 加密模式
    AES_256_GCM2 = 8

# 扩展服务内的错误处理策略
class ExtensionErrorHandlePolicy(Enum):
    # 当前扩展服务出错时, 停止其他扩展服务
    ERROR_ABORT = 'error_abort'
    # 当前扩展服务出错时, 其他扩展服务不受影响
    ERROR_IGNORE = 'error_ignore'

# 扩展服务的名称
class ExtensionServiceName(Enum):
    # 代表扩展服务为页面录制
    WEB_RECORDER_SERVICE = 'web_recorder_service'
    # 代表扩展服务为转推页面录制到 CDN
    RTMP_PUBLISH_SERVICE = 'rtmp_publish_service'

# 将订阅内容上传至扩展服务的状态
class ExtensionServiceState(Enum):
    # 服务正在初始化
    INIT = 'init'
    # 服务启动完成, 正在进行中
    IN_PROGRESS = 'inProgress'
    # 服务退出
    EXIT = 'exit'

# 服务类型
class ExtensionServiceStateName(Enum):
    # 上传服务
    UPLOAD_SERVICE = 'upload_service'
    # 页面录制服务
    WEB_RECORDER_SERVICE = 'web_recorder_service'

# 视频合流布局
class MixedVideoLayout(Enum):
    # 悬浮布局
    FLOATING = 0
    # 自适应布局
    ADAPTIVE = 1
    # 垂直布局
    VERTICAL = 2
    # 自定义布局
    CUSTOM = 3

# 录制模式
class Mode(Enum):
    # 单流录制模式
    INDIVIDUAL = 'individual'
    # 合流录制模式
    MIX = 'mix'
    # 页面录制模式
    WEB = 'web'

# 延时转码模式
class PostponeTranscodeMode(Enum):
    # 延时转码
    POSTPONE_TRANSCODING = 'postponeTranscoding'
    # 延时混音
    AUDIO_MIX = 'audioMix'

# 指定使用某个区域的资源进行录制
class RegionAffinity(Enum):
    # 根据发起请求的区域就近调用资源
    NEAR = 0
    # 中国
    CHINA = 1
    # 东南亚
    SOUTHEAST_ASIA = 2
    # 欧洲
    EUROPE = 3
    # 北美
    NORTH_AMERICA = 4

# 画面显示模式
class RenderMode(Enum):
    # 裁剪模式
    CROP = 0
    # 缩放模式
    SCALE = 1

# 云端录制资源使用场景
class Scene(Enum):
    # 实时音视频录制
    RTC = 0
    # 页面录制
    WEB = 1
    # 单流录制模式, 且开启延时转码或延时混音
    INDIVIDUAL_POSTPONE = 2

# 当前云服务的状态
class ServiceStatus(Enum):
    # 没有开始云服务
    NOT_STARTED = 0
    # 云服务初始化完成
    INITIALIZED = 1
    # 云服务组件开始启动
    STARTING = 2
    # 云服务部分组件启动完成
    PARTIAL_STARTED = 3
    # 云服务所有组件启动完成
    ALL_STARTED = 4
    # 云服务正在进行中
    IN_PROGRESS = 5
    # 云服务收到停止请求
    STOP_REQUESTED = 6
    # 云服务所有组件均停止
    ALL_STOPPED = 7
    # 云服务已退出
    EXITED = 8
    # 云服务异常退出
    EXCEPTION_EXITED = 20

# 截图文件类型
class SnapshotFileType(Enum):
    JPG = 'jpg'

# 视频截图类型
class SnapshotType(Enum):
    # 仅截图, 不录制
    SNAPSHOT_NO_RECORDING = 0
    # 录制并截图
    SNAPSHOT_AND_RECORDING = 1

# 第三方云存储平台
class StorageVendor(Enum):
    # Amazon S3
    AMAZON_S3 = 1
    # 阿里云
    ALIYUN_OSS = 2
    # 腾讯云
    TENCENT_CLOUD = 3
    # Microsoft Azure
    MICROSOFT_AZURE = 5
    # 谷歌云
    GOOGLE_CLOUD = 6
    # 华为云
    HUAWEI_CLOUD = 7
    # 百度智能云
    BAIDU_CLOUD = 8

# 媒体流的输出模式
class StreamMode(Enum):
    # 默认模式
    DEFAULT = 'default'
    # 标准模式
    STANDARD = 'standard'
    # 原始编码模式
    ORIGINAL = 'original'

# 订阅的媒体流类型
class StreamTypes(Enum):
    # 仅订阅音频
    AUDIO_ONLY = 0
    # 仅订阅视频
    VIDEO_ONLY = 1
    # 订阅音频和视频
    AUDIO_AND_VIDEO = 2

# 预估的订阅人数峰值
class SubscribeUidGroup(Enum):
    # 1 到 2 个 UID
    UID_1_2 = 0
    # 3 到 7 个 UID
    UID_3_7 = 1
    # 8 到 12 个 UID
    UID_8_12 = 2
    # 13 到 17 个 UID
    UID_13_17 = 3
    # 17 到 32 个 UID
    UID_17_32 = 4
    # 32 到 49 个 UID
    UID_32_49 = 5

# 当前录制上传的状态
class UploadingStatus(Enum):
    # 本次录制的文件已经全部上传至指定的第三方云存储
    UPLOADED = 'uploaded'
    # 本次录制的文件已经全部上传完成, 但是至少有一个 TS 文件上传到了声网备份云. 声网服务器会自动将这部分文件继续上传至指定的第三方云存储
    BACKED_UP = 'backuped'
    # 未知状态
    UNKNOWN = 'unknown'

# 订阅的视频流类型
class VideoStreamType(Enum):
    # 视频大流
    BIG_STREAM = 0
    # 视频小流
    SMALL_STREAM = 1

