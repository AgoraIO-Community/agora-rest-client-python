import logging
import os
from agora_rest_client.core import exceptions
from agora_rest_client.core.domain import RegionArea
from agora_rest_client.services.cloud_recording.v1.web_recording.web_recording_client import WebRecordingClient

if __name__ == '__main__':
    # 配置认证信息
    # 请勿将认证信息硬编码到代码中, 有安全风险
    # 可通过环境变量等方式配置认证信息
    # Need to set environment variable AGORA_APP_ID
    app_id = os.environ.get('AGORA_APP_ID')
    # Need to set environment variable AGORA_BASIC_AUTH_USER_NAME
    basic_auth_user_name = os.environ.get('AGORA_BASIC_AUTH_USER_NAME')
    # Need to set environment variable AGORA_BASIC_AUTH_PASSWORD
    basic_auth_password = os.environ.get('AGORA_BASIC_AUTH_PASSWORD')

    # 通过 acquire 请求获取到的 Resource ID
    resource_id = 'resource_id_xxx'
    # 通过 start 获取的录制 ID
    sid = 'sid_xxx'

    # 创建服务客户端
    web_recording_client = WebRecordingClient \
        .new_builder() \
        .with_app_id(app_id) \
        .with_basic_auth(basic_auth_user_name, basic_auth_password) \
        .with_region(RegionArea.CN.value) \
        .with_stream_log(log_level=logging.DEBUG) \
        .with_file_log(path='test.log') \
        .build()

    # 发送请求并获取响应
    try:
        response = web_recording_client.query(resource_id, sid)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.error_code)
        print(e.error_msg)

    os._exit(1)