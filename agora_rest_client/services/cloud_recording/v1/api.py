from enum import Enum

# 视频文件类型
class AvFileType():
    HLS = 'hls'
    MP4 = 'mp4'

# 录制模式
class Mode(Enum):
    # 单流录制模式
    INDIVIDUAL = 'individual'
    # 合流录制模式
    MIX = 'mix'
    # 页面录制模式
    WEB = 'web'

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

# 云端录制资源使用场景
class Scene(Enum):
    # 实时音视频录制
    RTC = 0
    # 页面录制
    WEB = 1
    # 单流录制模式, 且开启延时转码或延时混音
    INDIVIDUAL_POSTPONE = 2

# 视频截图类型
class SnapshotType(Enum):
    # 仅截图, 不录制
    SNAPSHOT_NO_RECORDING = 0
    # 录制并截图
    SNAPSHOT_AND_RECORDING = 1
