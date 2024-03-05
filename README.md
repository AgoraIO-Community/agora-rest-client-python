# Agora REST Client for Python
`agora-rest-client-python` 是用 Python 语言编写的一个开源项目, 专门为 Agora REST API 设计. 它包含了 Agora 官方提供的 REST API 接口的包装和内部实现, 可以帮助开发者更加方便的集成服务端Agora REST API.

## 特性
* 封装了 Agora REST API 的请求和响应处理, 简化与 Agora REST API 的通信流程
* 当遇到 DNS 解析失败/网络错误或者请求超时等问题的时候, 提供了自动切换最佳域名的能力, 以保障请求 REST API 服务的可用性
* 提供了易于使用的 API, 可轻松地实现调用 Agora REST API 的常见功能, 如开启云录制/停止云录制等

## 支持的服务
* [云端录制 Cloud Recording ](./agora_rest_client/services/cloud_recording/README.md)

## 环境准备
* [Python3.3 或以上版本](http://python.org/)
* 在声网 [Console 平台](https://console.shengwang.cn/)申请的 App ID 和 App Certificate
* 在声网 [Console 平台](https://console.shengwang.cn/)的 Basic Auth 认证信息
* 在声网 [Console 平台](https://console.shengwang.cn/)开启相关的服务能力

## 安装
您可以使用 pip 安装 SDK 依赖包, 也可以使用源码安装 SDK 依赖包.

- 使用 pip 安装
```shell
pip install agora_rest_client
```

- 使用源码安装
```shell
cd agora-rest-client-python
python setup.py install
```

## 使用示例
以调用云录制服务网页录制模式为例:
```python
import logging
import os
from agora_rest_client.core import exceptions
from agora_rest_client.core.domain import Domain
from agora_rest_client.core.domain import EndpointRegion
from agora_rest_client.services.cloud_recording.v1.api import ExtensionServiceName
from agora_rest_client.services.cloud_recording.v1.web_recording import api_start
from agora_rest_client.services.cloud_recording.v1.web_recording.web_recording_client import WebRecordingClient

if __name__ == '__main__':
    # 配置认证信息
    # 请勿将认证信息硬编码到代码中, 有安全风险
    # 可通过环境变量等方式配置认证信息
    # Need to set environment variable AGORA_APP_ID
    app_id = os.environ.get('AGORA_APP_ID')
    # Need to set environment variable AGORA_CREDENTIAL_BASIC_AUTH_USER_NAME
    credential_basic_auth_user_name = os.environ.get('AGORA_CREDENTIAL_BASIC_AUTH_USER_NAME')
    # Need to set environment variable AGORA_CREDENTIAL_BASIC_AUTH_PASSWORD
    credential_basic_auth_password = os.environ.get('AGORA_CREDENTIAL_BASIC_AUTH_PASSWORD')
    # 第三方云存储配置
    storage_config_region = int(os.environ.get('AGORA_STORAGE_CONFIG_REGION'))
    storage_config_vendor = int(os.environ.get('AGORA_STORAGE_CONFIG_VENDOR'))
    storage_config_bucket = os.environ.get('AGORA_STORAGE_CONFIG_BUCKET')
    storage_config_access_key = os.environ.get('AGORA_STORAGE_CONFIG_ACCESS_KEY')
    storage_config_secret_key = os.environ.get('AGORA_STORAGE_CONFIG_SECRET_KEY')

    # 通过 acquire 请求获取到的 Resource ID
    resource_id = 'resource_id_xxx'
    # 录制的频道名
    cname = 'cname_xxx'
    # 字符串内容为云端录制服务在 RTC 频道内使用的 UID, 用于标识频道内的录制服务
    uid = '123456'

    # 创建服务客户端
    web_recording_client = WebRecordingClient \
        .new_builder() \
        .with_app_id(app_id) \
        .with_credential_basic_auth(credential_basic_auth_user_name, credential_basic_auth_password) \
        .with_domain(Domain(EndpointRegion.CN.value)) \
        .with_stream_log(log_level=logging.DEBUG) \
        .with_file_log(path='test.log') \
        .build()

    # 发送请求并获取响应
    try:
        response = web_recording_client.start(resource_id, cname, uid, storage_config=api_start.StorageConfig(
            region=storage_config_region,
            vendor=storage_config_vendor,
            bucket=storage_config_bucket,
            accessKey=storage_config_access_key,
            secretKey=storage_config_secret_key
        ), extension_service_config=api_start.ExtensionServiceConfig(
            extensionServices=[
                api_start.ExtensionServices(
                    serviceName=ExtensionServiceName.WEB_RECORDER_SERVICE.value,
                    serviceParam=api_start.ServiceParam(
                        url="https://www.agora.io",
                        audioProfile=2,
                        videoWidth=1280,
                        videoHeight=720,
                        maxRecordingHour=1
                    )
                )
            ]
        ))
        print(response)
    except exceptions.ClientException as e:
        print(e.status_code)
        print(e.error_code)
        print(e.error_msg)
```
更多的示例可在[Example](./examples) 查看

## 集成遇到困难, 该如何联系声网获取协助
> 方案1: 如果您已经在使用声网服务或者在对接中, 可以直接联系对接的销售或服务
>
> 方案2: 发送邮件给 [support@agora.io](mailto:support@agora.io) 咨询
>
> 方案3: 扫码加入我们的微信交流群提问
>
> <img src="https://download.agora.io/demo/release/SDHY_QA.jpg" width="360" height="360">
---

## 贡献
本项目欢迎并接受贡献. 如果您在使用中遇到问题或有改进建议, 请提出issue或向我们提交Pull Request.

# SemVer 版本规范
本项目使用语义化版本号规范 (SemVer) 来管理版本. 格式为 MAJOR.MINOR.PATCH.

* MAJOR 版本号表示不向后兼容的重大更改.
* MINOR 版本号表示向后兼容的新功能或增强.
* PATCH 版本号表示向后兼容的错误修复和维护.
有关详细信息, 请参阅 [语义化版本](https://semver.org/lang/zh-CN/) 规范.

## 参考
* [Agora API 文档](https://doc.shengwang.cn/)

## 许可证
该项目使用MIT许可证, 详细信息请参阅LICENSE文件._