class FileList(object):
    filename = None
    sliceStartTime = None
    
class Payload(object):
    fileList = [FileList()]
    onhold = None
    state = None
    
class ExtensionServiceState(object):
    payload = Payload()
    serviceName = None

class ServerResponse(object):
    status = None
    extensionServiceState = [ExtensionServiceState()]

class RequestPathParamsApiQuery(object):
    # 录制模式, 参考 Mode 枚举类. 传入字符串, 如 Mode.INDIVIDUAL.value
    mode = None
    # 通过 acquire 请求获取到的 Resource ID
    resource_id = None
    # 通过 start 获取的录制 ID
    sid = None

    def __init__(self, d):
        self.__dict__.update(d)

    def __str__(self):
        return ",".join(["{}={}".format(k, v) for k, v in self.__dict__.items()])

class ResponseApiQuery(object):
    resourceId = None
    sid = None
    serverResponse = ServerResponse()
    cname = None
    uid = None

    def __init__(self, d):
        self.__dict__.update(d)

    def __str__(self):
        return ",".join(["{}={}".format(k, v) for k, v in self.__dict__.items()])

def api_query(client, request_path_params_obj, response_type, response_obj=ResponseApiQuery):
    """
    :param client: CloudRecordingClient object
    :param request_path_params_obj: request object RequestApiQuery
    :param response_type: response type
    :param response_obj: response object
    :return: response object ResponseApiQuery
    """
    url = '/v1/apps/{}/cloud_recording/resourceid/{}/sid/{}/mode/{}/query'.format(client.app_id, request_path_params_obj.resource_id, request_path_params_obj.sid, request_path_params_obj.mode)
    client.logger.debug("url:%s", url)

    return client.call_api('GET', url, response_type=response_type, response_obj=response_obj)
