from agora_rest_client.services.cloud_recording.v1.cloud_recording_client import CloudRecordingClient
from agora_rest_client.services.cloud_recording.v1.web_recording.api_acquire import web_recording_acquire
from agora_rest_client.services.cloud_recording.v1.web_recording.api_query import web_recording_query
from agora_rest_client.services.cloud_recording.v1.web_recording.api_start import web_recording_start
from agora_rest_client.services.cloud_recording.v1.web_recording.api_stop import web_recording_stop
from agora_rest_client.services.cloud_recording.v1.web_recording.api_update import web_recording_update

class WebRecordingClient(CloudRecordingClient):
    """
    Web recording client
    """

    def __init__(self):
        super(WebRecordingClient, self).__init__()

    def new_builder():
        return WebRecordingClient()

    def acquire(self, cname, uid, resource_expired_hour=None, exclude_resource_ids=None, region_affinity=None, trace_id=None):
        """
        Web recoding acquire
        获取云端录制资源

        :type client: object
        :param client: WebRecordingClient object

        :type cname: str
        :param cname: cname
        :refer: `agora_rest_client.services.cloud_recording.v1.api_acquire.RequestBodyApiAcquire.cname`

        :type uid: str
        :param uid: uid
        :refer: `agora_rest_client.services.cloud_recording.v1.api_acquire.RequestBodyApiAcquire.uid`

        :type resource_expired_hour: int
        :param resource_expired_hour: resource expired hour
        :refer: `agora_rest_client.services.cloud_recording.v1.api_acquire.ClientRequest.resourceExpiredHour`

        :type exclude_resource_ids: list
        :param exclude_resource_ids: exclude resource ids
        :refer: `agora_rest_client.services.cloud_recording.v1.api_acquire.ClientRequest.excludeResourceIds`

        :type region_affinity: int
        :param region_affinity: region affinity
        :refer: `agora_rest_client.services.cloud_recording.v1.api_acquire.ClientRequest.regionAffinity`
        :value: enum of `agora_rest_client.services.cloud_recording.v1.api.RegionAffinity`

        :type trace_id: string
        :param trace_id: trace id

        :return: response object ResponseApiAcquire
        """
        return web_recording_acquire(self, cname, uid, resource_expired_hour=resource_expired_hour, exclude_resource_ids=exclude_resource_ids,
                                     region_affinity=region_affinity, trace_id=trace_id)

    def query(self, resource_id, sid, trace_id=None):
        """
        Web recording query
        查询云端录制状态

        :type client: object
        :param client: WebRecordingClient object

        :type resource_id: str
        :param resource_id: resource id
        :refer: `agora_rest_client.services.cloud_recording.v1.api_query.RequestPathParamsApiQuery.resource_id`

        :type sid: str
        :param sid: sid
        :refer: `agora_rest_client.services.cloud_recording.v1.api_query.RequestPathParamsApiQuery.sid`

        :type trace_id: string
        :param trace_id: trace id

        :return: response object ResponseApiQuery
        """
        return web_recording_query(self, resource_id, sid, trace_id=trace_id)

    def start(self, resource_id, cname, uid, storage_config, extension_service_config, trace_id=None):
        """
        Web recording start
        开始云端录制

        :type client: object
        :param client: WebRecordingClient object

        :type resource_id: str
        :param resource_id: resource id
        :refer: `agora_rest_client.services.cloud_recording.v1.api_start.RequestPathParamsApiStart.resource_id`

        :type cname: str
        :param cname: cname
        :refer: `agora_rest_client.services.cloud_recording.v1.api_start.RequestBodyApiStart.cname`

        :type uid: str
        :param uid: uid
        :refer: `agora_rest_client.services.cloud_recording.v1.api_start.RequestBodyApiStart.uid`

        :type storage_config: object
        :param storage_config: storage config
        :refer: `agora_rest_client.services.cloud_recording.v1.api_start.StorageConfig`
        :value: instance of `agora_rest_client.services.cloud_recording.v1.web_recording.api_start.StorageConfig`

        :type extension_service_config: object
        :param extension_service_config: extension service config
        :refer: `agora_rest_client.services.cloud_recording.v1.api_start.ExtensionServiceConfig`
        :value: instance of `agora_rest_client.services.cloud_recording.v1.web_recording.api_start.ExtensionServiceConfig`

        :type trace_id: string
        :param trace_id: trace id

        :return: response object ResponseApiStart
        """
        return web_recording_start(self, resource_id, cname, uid, storage_config, extension_service_config, trace_id=trace_id)

    def stop(self, resource_id, sid, cname, uid, async_stop=False, trace_id=None):
        """
        Web recording stop
        停止云端录制

        :type client: object
        :param client: WebRecordingClient object

        :type resource_id: str
        :param resource_id: resource id
        :refer: `agora_rest_client.services.cloud_recording.v1.api_stop.RequestPathParamsApiStop.resource_id`

        :type sid: str
        :param sid: sid
        :refer: `agora_rest_client.services.cloud_recording.v1.api_stop.RequestPathParamsApiStop.sid`

        :type cname: str
        :param cname: cname
        :refer: `agora_rest_client.services.cloud_recording.v1.api_stop.RequestBodyApiStop.cname`

        :type uid: str
        :param uid: uid
        :refer: `agora_rest_client.services.cloud_recording.v1.api_stop.RequestBodyApiStop.uid`

        :type async_stop: bool
        :param async_stop: async stop
        :refer: `agora_rest_client.services.cloud_recording.v1.api_stop.ClientRequest.async_stop`

        :type trace_id: string
        :param trace_id: trace id

        :return: response object ResponseApiStop
        """
        return web_recording_stop(self, resource_id, sid, cname, uid, async_stop=async_stop, trace_id=trace_id)

    def update(self, resource_id, sid, cname, uid, web_recording_config=None, rtmp_publish_config=None, trace_id=None):
        """
        Web recording update
        更新云端录制设置

        :type client: object
        :param client: WebRecordingClient object

        :type resource_id: str
        :param resource_id: resource id
        :refer: `agora_rest_client.services.cloud_recording.v1.api_update.RequestPathParamsApiUpdate.resource_id`

        :type sid: str
        :param sid: sid
        :refer: `agora_rest_client.services.cloud_recording.v1.api_update.RequestPathParamsApiUpdate.sid`

        :type cname: str
        :param cname: cname
        :refer: `agora_rest_client.services.cloud_recording.v1.api_update.RequestBodyApiUpdate.cname`

        :type uid: str
        :param uid: uid
        :refer: `agora_rest_client.services.cloud_recording.v1.api_update.RequestBodyApiUpdate.uid`

        :type web_recording_config: object
        :param web_recording_config: web recording config
        :refer: `agora_rest_client.services.cloud_recording.v1.api_update.WebRecordingConfig`
        :value: instance of `agora_rest_client.services.cloud_recording.v1.web_recording.api_update.WebRecordingConfig`

        :type rtmp_publish_config: object
        :param rtmp_publish_config: rtmp publish config
        :refer: `agora_rest_client.services.cloud_recording.v1.api_update.RtmpPublishConfig`
        :value: instance of `agora_rest_client.services.cloud_recording.v1.web_recording.api_update.RtmpPublishConfig`

        :type trace_id: string
        :param trace_id: trace id

        :return: response object ResponseApiUpdate
        """
        return web_recording_update(self, resource_id, sid, cname, uid, web_recording_config=web_recording_config,
                                    rtmp_publish_config=rtmp_publish_config, trace_id=trace_id)
