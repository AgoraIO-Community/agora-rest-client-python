# 云端录制服务
## 服务简介
云端录制是声网为音视频通话和直播研发的录制组件, 提供 RESTful API 供开发者实现录制功能, 并将录制文件存至第三方云存储. 云端录制有稳定可靠/简单易用/成本可控/方案灵活/支持私有化部署等优势, 是在线教育/视频会议/金融监管/客户服务场景的理想录制方案. 

## 环境准备
- 获取声网App ID -------- [声网Agora - 文档中心 - 如何获取 App ID](https://docs.agora.io/cn/Agora%20Platform/get_appid_token?platform=All%20Platforms#%E8%8E%B7%E5%8F%96-app-id)

  > - 点击创建应用
  >
  >   ![](https://accktvpic.oss-cn-beijing.aliyuncs.com/pic/github_readme/create_app_1.jpg)
  >
  > - 选择您要创建的应用类型
  >
  >   ![](https://accktvpic.oss-cn-beijing.aliyuncs.com/pic/github_readme/create_app_2.jpg)

- 获取App 证书 ----- [声网Agora - 文档中心 - 获取 App 证书](https://docs.agora.io/cn/Agora%20Platform/get_appid_token?platform=All%20Platforms#%E8%8E%B7%E5%8F%96-app-%E8%AF%81%E4%B9%A6)

  > 在声网控制台的项目管理页面, 找到您的项目, 点击配置. 
  > ![](https://fullapp.oss-cn-beijing.aliyuncs.com/scenario_api/callapi/config/1641871111769.png)
  > 点击主要证书下面的复制图标, 即可获取项目的 App 证书. 
  > ![](https://fullapp.oss-cn-beijing.aliyuncs.com/scenario_api/callapi/config/1637637672988.png)

- 开启云录制服务
  > ![](https://fullapp.oss-cn-beijing.aliyuncs.com/scenario_api/callapi/config/rtm_config1.jpg)
  > ![](https://fullapp.oss-cn-beijing.aliyuncs.com/scenario_api/callapi/config/rtm_config2.jpg)  
  > ![](https://fullapp.oss-cn-beijing.aliyuncs.com/agora-rest-client/go/open_cloud_recording.png)

## API V1 接口调用示例
### 获取云端录制资源
> 在开始云端录制之前, 您需要调用 acquire 方法获取一个 Resource ID. 一个 Resource ID 只能用于一次云端录制服务. 

#### 单流录制
通过调用`individual_recording_client.acquire`方法来实现获取录制资源
```python
individual_recording_client = individual_recording_client.IndividualRecordingClient \
    .new_builder() \
    .with_app_id(app_id) \
    .with_basic_auth(basic_auth_user_name, basic_auth_password) \
    .with_region(RegionArea.CN.value) \
    .with_stream_log(log_level=logging.DEBUG) \
    .with_file_log(path='test.log') \
    .build()

try:
    response = individual_recording_client.acquire(cname, uid)
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.error_code)
    print(e.error_msg)
```
具体可参考 Example [individual_recording/example_api.py](../../../examples/cloud_recording/v1/individual_recording/example_api.py) 文件

#### 合流录制
通过调用`mix_recording_client.acquire`方法来实现获取录制资源
```python
mix_recording_client = mix_recording_client.MixRecordingClient \
    .new_builder() \
    .with_app_id(app_id) \
    .with_basic_auth(basic_auth_user_name, basic_auth_password) \
    .with_region(RegionArea.CN.value) \
    .with_stream_log(log_level=logging.DEBUG) \
    .with_file_log(path='test.log') \
    .build()

try:
    response = mix_recording_client.acquire(cname, uid)
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.error_code)
    print(e.error_msg)
```
具体可参考 Example [mix_recording/example_api.py](../../../examples/cloud_recording/v1/mix_recording/example_api.py) 文件

#### 网页录制
通过调用`web_recording_client.acquire`方法来实现获取录制资源
```python
web_recording_client = WebRecordingClient \
    .new_builder() \
    .with_app_id(app_id) \
    .with_basic_auth(basic_auth_user_name, basic_auth_password) \
    .with_region(RegionArea.CN.value) \
    .with_stream_log(log_level=logging.DEBUG) \
    .with_file_log(path='test.log') \
    .build()

try:
    response = web_recording_client.acquire(cname, uid)
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.error_code)
    print(e.error_msg)
```
具体可参考 Example [web_recording/example_api.py](../../../examples/cloud_recording/v1/web_recording/example_api.py) 文件

### 开始云端录制
> 通过 acquire 方法获取云端录制资源后, 调用 start 方法开始云端录制. 

#### 单流录制
通过调用`individual_recording_client.start`方法来实现开始录制
```python
try:
    response = individual_recording_client.start(resource_id, cname, uid, token, 
        storage_config=api_start.StorageConfig(
            region=storage_config_region,
            vendor=storage_config_vendor,
            bucket=storage_config_bucket,
            accessKey=storage_config_access_key,
            secretKey=storage_config_secret_key
        )
    )
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.error_code)
    print(e.error_msg)
```
具体可参考 Example [individual_recording/example_api.py](../../../examples/cloud_recording/v1/individual_recording/example_api.py) 文件

#### 合流录制
通过调用`mix_recording_client.start`方法来实现开始录制
```python
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
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.error_code)
    print(e.error_msg)
```
具体可参考 Example [mix_recording/example_api.py](../../../examples/cloud_recording/v1/mix_recording/example_api.py) 文件

#### 网页录制
通过调用`web_recording_client.start`方法来实现开始录制
```python
try:
    response = web_recording_client.start(resource_id, cname, uid, 
        storage_config=api_start.StorageConfig(
            region=storage_config_region,
            vendor=storage_config_vendor,
            bucket=storage_config_bucket,
            accessKey=storage_config_access_key,
            secretKey=storage_config_secret_key
        ), 
        extension_service_config=api_start.ExtensionServiceConfig(
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
        )
    )
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.error_code)
    print(e.error_msg)
```
具体可参考 Example [web_recording/example_api.py](../../../examples/cloud_recording/v1/web_recording/example_api.py) 文件

### 停止云端录制
> 开始录制后, 您可以调用 stop 方法离开频道, 停止录制. 录制停止后如需再次录制, 必须再调用 acquire 方法请求一个新的 Resource ID. 

#### 单流录制
通过调用`individual_recording_client.stop`方法来实现停止录制
```python
try:
    response = individual_recording_client.stop(resource_id, sid, cname, uid)
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.error_code)
    print(e.error_msg)
```
具体可参考 Example [individual_recording/example_api.py](../../../examples/cloud_recording/v1/individual_recording/example_api.py) 文件

#### 合流录制
通过调用`mix_recording_client.stop`方法来实现停止录制
```python
try:
    response = mix_recording_client.stop(resource_id, sid, cname, uid)
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.error_code)
    print(e.error_msg)
```
具体可参考 Example [mix_recording/example_api.py](../../../examples/cloud_recording/v1/mix_recording/example_api.py) 文件

#### 网页录制
通过调用`web_recording_client.stop`方法来实现停止录制
```python
try:
    response = web_recording_client.stop(resource_id, sid, cname, uid)
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.error_code)
    print(e.error_msg)
```
具体可参考 Example [web_recording/example_api.py](../../../examples/cloud_recording/v1/web_recording/example_api.py) 文件

### 查询云端录制状态
> 开始录制后, 您可以调用 query 方法查询录制状态. 

#### 单流录制
通过调用`individual_recording_client.query`方法来实现查询录制状态
```python
try:
    response = individual_recording_client.query(resource_id, sid)
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.error_code)
    print(e.error_msg)
```
具体可参考 Example [individual_recording/example_api.py](../../../examples/cloud_recording/v1/individual_recording/example_api.py) 文件

#### 合流录制
通过调用`mix_recording_client.query`方法来实现查询录制状态
```python
try:
    response = mix_recording_client.query(resource_id, sid)
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.error_code)
    print(e.error_msg)
```
具体可参考 Example [mix_recording/example_api.py](../../../examples/cloud_recording/v1/mix_recording/example_api.py) 文件

#### 网页录制
通过调用`web_recording_client.query`方法来实现查询录制状态
```python
try:
    response = web_recording_client.query(resource_id, sid)
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.error_code)
    print(e.error_msg)
```
具体可参考 Example [web_recording/example_api.py](../../../examples/cloud_recording/v1/web_recording/example_api.py) 文件

### 更新云端录制设置
> 开始录制后, 您可以调用 update 方法更新如下录制配置: 
> * 对单流录制和合流录制, 更新订阅名单. 
> * 对页面录制, 设置暂停/恢复页面录制, 或更新页面录制转推到 CDN 的推流地址(URL). 

#### 单流录制
通过调用`individual_recording_client.update`方法来实现更新录制设置
```python
try:
    response = individual_recording_client.update(resource_id, sid, cname, uid, 
        stream_subscribe=api_update.StreamSubscribe(
            videoUidList=api_update.VideoUidList(
                subscribeVideoUids=["#allstream#"]
            )
        )
    )
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.error_code)
    print(e.error_msg)
```
具体可参考 Example [individual_recording/example_api.py](../../../examples/cloud_recording/v1/individual_recording/example_api.py) 文件

#### 合流录制
通过调用`mix_recording_client.update`方法来实现更新录制设置
```python
try:
    response = mix_recording_client.update(resource_id, sid, cname, uid, 
        stream_subscribe=api_update.StreamSubscribe(
            videoUidList=api_update.VideoUidList(
                subscribeVideoUids=["#allstream#"]
            )
        )
    )
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.error_code)
    print(e.error_msg)
```
具体可参考 Example [mix_recording/example_api.py](../../../examples/cloud_recording/v1/mix_recording/example_api.py) 文件

#### 网页录制
通过调用`web_recording_client.update`方法来实现更新录制设置
```python
try:
    response = web_recording_client.update(resource_id, sid, cname, uid, web_recording_config=api_update.WebRecordingConfig(onhold=True))
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.error_code)
    print(e.error_msg)
```
具体可参考 Example [web_recording/example_api.py](../../../examples/cloud_recording/v1/web_recording/example_api.py) 文件

### 更新云端录制合流布局
> 开始录制后, 您可以调用 updateLayout 方法更新合流布局. 
> 每次调用该方法都会覆盖原来的布局设置. 例如, 在开始录制时设置了 backgroundColor 为 "#FF0000"(红色), 如果调用 updateLayout 方法更新合流布局时如果不再设置 backgroundColor 字段, 背景色就会变为黑色(默认值). 

#### 合流录制
通过调用`mix_recording_client.update_layout`方法来实现更新录制设置
```python
try:
    response = mix_recording_client.update_layout(resource_id, sid, cname, uid, mixed_video_layout=1)
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.error_code)
    print(e.error_msg)
```
具体可参考 Example [mix_recording/example_api.py](../../../examples/cloud_recording/v1/mix_recording/example_api.py) 文件

### Example 示例
- 单流录制 Example [individual_recording/example_api.py](../../../examples/cloud_recording/v1/individual_recording/example_api.py) 文件
- 合流录制 Example [mix_recording/example_api.py](../../../examples/cloud_recording/v1/mix_recording/example_api.py) 文件
- 网页录制 Example [web_recording/example_api.py](../../../examples/cloud_recording/v1/web_recording/example_api.py) 文件

## 错误码和响应状态码处理
具体的业务响应码请参考[业务响应码](https://doc.shengwang.cn/api-ref/cloud-recording/restful/response-code)文档