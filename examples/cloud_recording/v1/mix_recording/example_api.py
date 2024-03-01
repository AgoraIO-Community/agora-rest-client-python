import logging
import os
from agora_rest_client.core import exceptions
from agora_rest_client.core.domain import RegionArea
from agora_rest_client.services.cloud_recording.v1.mix_recording import api_start
from agora_rest_client.services.cloud_recording.v1.mix_recording import api_update
from agora_rest_client.services.cloud_recording.v1.mix_recording import api_update_layout
from agora_rest_client.services.cloud_recording.v1.mix_recording import mix_recording_client

# Stop recording
def stop_recording(resource_id, sid, cname, uid):
    try:
        response = mix_recording_client.stop(resource_id, sid, cname, uid)
        mix_recording_client.logger.info('stop recording, response:%s', response)
    except exceptions.ClientException as e:
        mix_recording_client.logger.error('stop recording, err:%s', e)
        os._exit(1)

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
    # 第三方云存储配置
    storage_config_region = int(os.environ.get('AGORA_STORAGE_CONFIG_REGION'))
    storage_config_vendor = int(os.environ.get('AGORA_STORAGE_CONFIG_VENDOR'))
    storage_config_bucket = os.environ.get('AGORA_STORAGE_CONFIG_BUCKET')
    storage_config_access_key = os.environ.get('AGORA_STORAGE_CONFIG_ACCESS_KEY')
    storage_config_secret_key = os.environ.get('AGORA_STORAGE_CONFIG_SECRET_KEY')
    # 用于鉴权的动态密钥
    token = os.environ.get('AGORA_TOKEN')

    # 录制的频道名
    cname = os.environ.get('AGORA_CNAME')
    # 字符串内容为云端录制服务在 RTC 频道内使用的 UID, 用于标识频道内的录制服务
    uid = '123456'

    # 创建服务客户端
    mix_recording_client = mix_recording_client.MixRecordingClient \
        .new_builder() \
        .with_app_id(app_id) \
        .with_basic_auth(basic_auth_user_name, basic_auth_password) \
        .with_region(RegionArea.CN.value) \
        .with_stream_log(log_level=logging.DEBUG) \
        .with_file_log(path='test.log') \
        .build()

    # 发送请求并获取响应
    # Acquire resource
    try:
        response = mix_recording_client.acquire(cname, uid)
        mix_recording_client.logger.info('acquire resource, cname:%s, uid:%s, response:%s', cname, uid, response)
    except exceptions.ClientException as e:
        mix_recording_client.logger.error('acquire resource, , cname:%s, uid:%s, err:%s', cname, uid, e)
        os._exit(1)

    resource_id = response.resourceId

    # Start recording
    try:
        response = mix_recording_client.start(resource_id, cname, uid, token,
            storage_config=api_start.StorageConfig(
                region=storage_config_region,
                vendor=storage_config_vendor,
                bucket=storage_config_bucket,
                accessKey=storage_config_access_key,
                secretKey=storage_config_secret_key
            )
        )
        mix_recording_client.logger.info('start recording, resource_id:%s, response:%s', resource_id, response)
    except exceptions.ClientException as e:
        mix_recording_client.logger.error('start recording, resource_id:%s, err:%s', resource_id, e)
        os._exit(1)

    sid = response.sid

    # Query recording
    try:
        response = mix_recording_client.query(resource_id, sid)
        mix_recording_client.logger.info('query recording, sid:%s, response:%s', sid, response)
    except exceptions.ClientException as e:
        mix_recording_client.logger.error('query recording, sid:%s, err:%s', sid, e)
        stop_recording(resource_id, sid, cname, uid)
        os._exit(1)

    # Update recording
    try:
        response = mix_recording_client.update(resource_id, sid, cname, uid,
            stream_subscribe=api_update.StreamSubscribe(
                videoUidList=api_update.VideoUidList(
                    subscribeVideoUids=["#allstream#"]
                )
            )
        )
        mix_recording_client.logger.info('update recording, response:%s', response)
    except exceptions.ClientException as e:
        mix_recording_client.logger.error('update recording, err:%s', e)
        stop_recording(resource_id, sid, cname, uid)
        os._exit(1)

    # Update layout recording
    try:
        response = mix_recording_client.update_layout(resource_id, sid, cname, uid, mixed_video_layout=1)
        mix_recording_client.logger.info('update layout recording, response:%s', response)
    except exceptions.ClientException as e:
        mix_recording_client.logger.error('update layout recording, err:%s', e)
        stop_recording(resource_id, sid, cname, uid)
        os._exit(1)

    # Stop recording
    stop_recording(resource_id, sid, cname, uid)
    os._exit(0)