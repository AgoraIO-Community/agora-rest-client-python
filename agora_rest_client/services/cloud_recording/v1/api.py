from enum import Enum

# 录制模式
class Mode(Enum):
    # 单流录制模式
    INDIVIDUAL = 'individual'
    # 合流录制模式
    MIX = 'mix'
    # 页面录制模式
    WEB = 'web'

# 云端录制资源使用场景
class Scene(Enum):
    # 实时音视频录制
    RTC = 0
    # 页面录制
    WEB = 1
    # 单流录制模式, 且开启延时转码或延时混音
    INDIVIDUAL_DELAY = 2

# 视频截图类型
class SnapshotType(Enum):
    # 仅截图, 不录制
    SNAPSHOT_NO_RECORDING = 0
    # 录制并截图
    SNAPSHOT_AND_RECORDING = 1
