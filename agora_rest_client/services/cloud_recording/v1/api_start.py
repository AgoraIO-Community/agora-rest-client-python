from agora_rest_client.core import utils

class ExtensionParams(object):
    sse = None
    tag = None

class StorageConfig(object):
    region = None
    vendor = None
    bucket = None
    accessKey = None
    secretKey = None
    fileNamePrefix = []
    extensionParams = ExtensionParams()

class LayoutConfig(object):
    uid = None
    x_axis = None
    y_axis = None
    width = None
    height = None
    alpha = None
    render_mode = None

class BackgroundConfig(object):
    uid = None
    image_url = None
    render_mode = None

class TranscodingConfig(object):
    width = None
    height = None
    fps = None
    bitrate = None
    maxResolutionUid = None
    mixedVideoLayout = None
    backgroundColor = None
    backgroundImage = None
    defaultUserBackgroundImage = None
    layoutConfig = [LayoutConfig()]
    backgroundConfig = [BackgroundConfig()]

class RecordingConfig(object):
    channelType = None
    decryptionMode = None
    secret = None
    salt = None
    maxIdleTime = None
    streamTypes = None
    videoStreamType = None
    subscribeAudioUids = []
    unsubscribeAudioUids = []
    subscribeVideoUids = []
    unsubscribeVideoUids = []
    subscribeUidGroup = None
    streamMode = None
    audioProfile = None
    audioProfile = None
    transcodingConfig = TranscodingConfig()

class RecordingFileConfig(object):
    avFileType = []

class SnapshotConfig(object):
    captureInterval = None
    fileType = []

class ServiceParam(object):
    url = None
    audioProfile = None
    videoWidth = None
    videoHeight = None
    maxRecordingHour = None
    videoBitrate = None
    videoFps = None
    mobile = None
    maxVideoDuration = None
    onhold = None
    readyTimeout = None

class ExtensionServices(object):
    serviceName = None
    errorHandlePolicy = None
    serviceParam = ServiceParam()

class ExtensionServiceConfig(object):
    errorHandlePolicy = None
    extensionServices = [ExtensionServices()]

class AppsCollection(object):
    combinationPolicy = None

class TransConfig(object):
    transMode = None

class Container(object):
    format = None

class Audio(object):
    sampleRate = None
    bitrate = None
    channels = None

class TranscodeOptions(object):
    transConfig = TransConfig()
    container = Container()
    audio = Audio()

class ClientRequest(object):
    token = None
    storageConfig = StorageConfig()
    recordingConfig = RecordingConfig()
    recordingFileConfig = RecordingFileConfig()
    snapshotConfig = SnapshotConfig()
    extensionServiceConfig = ExtensionServiceConfig()
    appsCollection = AppsCollection()
    transcodeOptions = TranscodeOptions()

class RequestPathParamsApiStart(object):
    # 录制模式, 参考 Mode 枚举类. 传入字符串, 如 Mode.INDIVIDUAL.value
    mode = None
    # 通过 acquire 请求获取到的 Resource ID
    resource_id = None

    def __init__(self, d):
        self.__dict__.update(d)

    def __str__(self):
        return ",".join(["{}={}".format(k, v) for k, v in self.__dict__.items()])

class RequestBodyApiStart(object):
    cname = None
    uid = None
    clientRequest = ClientRequest()

    def __init__(self, d):
        self.__dict__.update(d)

    def __str__(self):
        return ",".join(["{}={}".format(k, v) for k, v in self.__dict__.items()])

class ResponseApiStart(object):
    cname = None
    uid = None
    resourceId = None
    sid = None
    
    def __init__(self, d):
        self.__dict__.update(d)

    def __str__(self):
        return ",".join(["{}={}".format(k, v) for k, v in self.__dict__.items()])

def api_start(client, request_path_params_obj, request_body_obj, response_type, response_obj=ResponseApiStart):
    """
    :param client: CloudRecordingClient object
    :param request_path_params_obj: request object RequestPathParamsApiStart
    :param request_body_obj: request object RequestBodyApiStart
    :param response_type: response type
    :param response_obj: response object
    :return: response object ResponseApiStart
    """
    url = '/v1/apps/{}/cloud_recording/resourceid/{}/mode/{}/start'.format(client.app_id, request_path_params_obj.resource_id, request_path_params_obj.mode)
    client.logger.debug("url:%s", url)

    return client.call_api('POST', url, post_json=utils.to_json(request_body_obj), response_type=response_type, response_obj=response_obj)
