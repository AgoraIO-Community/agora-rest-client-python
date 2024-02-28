from enum import Enum

# 录制模式
class Mode(Enum):
    # 单流录制模式
    INDIVIDUAL = 'individual'
    # 合流录制模式
    MIX = 'mix'
    # 页面录制模式
    WEB = 'web'
