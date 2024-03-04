from agora_rest_client.services.cloud_recording.v1.cloud_recording_client import CloudRecordingClient
from agora_rest_client.services.cloud_recording.v1.mix_recording.api_acquire import mix_recording_acquire
from agora_rest_client.services.cloud_recording.v1.mix_recording.api_query import mix_recording_query
from agora_rest_client.services.cloud_recording.v1.mix_recording.api_start import mix_recording_start
from agora_rest_client.services.cloud_recording.v1.mix_recording.api_stop import mix_recording_stop
from agora_rest_client.services.cloud_recording.v1.mix_recording.api_update_layout import mix_recording_update_layout
from agora_rest_client.services.cloud_recording.v1.mix_recording.api_update import mix_recording_update

class MixRecordingClient(CloudRecordingClient):
    """
    Mix recording client
    """

    def __init__(self):
        super(MixRecordingClient, self).__init__()

    def new_builder():
        return MixRecordingClient()

    def acquire(self, cname, uid, resource_expired_hour=None, exclude_resource_ids=None, region_affinity=None, trace_id=None):
        """
        Mix recording acquire
        获取云端录制资源

        :type client: object
        :param client: MixRecordingClient object

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
        return mix_recording_acquire(self, cname, uid, resource_expired_hour=resource_expired_hour, exclude_resource_ids=exclude_resource_ids,
                                     region_affinity=region_affinity, trace_id=trace_id)

    def query(self, resource_id, sid, trace_id=None):
        """
        Mix recording query
        查询云端录制状态

        :type client: object
        :param client: MixRecordingClient object

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
        return mix_recording_query(self, resource_id, sid, trace_id=trace_id)

    def start(self, resource_id, cname, uid, token, storage_config, recording_config=None, trace_id=None):
        """
        Mix recording start
        开始云端录制

        :type client: object
        :param client: MixRecordingClient object

        :type resource_id: str
        :param resource_id: resource id
        :refer: `agora_rest_client.services.cloud_recording.v1.api_start.RequestPathParamsApiStart.resource_id`

        :type cname: str
        :param cname: cname
        :refer: `agora_rest_client.services.cloud_recording.v1.api_start.RequestBodyApiStart.cname`

        :type uid: str
        :param uid: uid
        :refer: `agora_rest_client.services.cloud_recording.v1.api_start.RequestBodyApiStart.uid`

        :type token: str
        :param token: token
        :refer: `agora_rest_client.services.cloud_recording.v1.api_start.ClientRequest.token`

        :type storage_config: object
        :param storage_config: storage config
        :refer: `agora_rest_client.services.cloud_recording.v1.api_start.StorageConfig`
        :value: instance of `agora_rest_client.services.cloud_recording.v1.mix_recording.api_start.StorageConfig`

        :type recording_config: object
        :param recording_config: recording config
        :refer: `agora_rest_client.services.cloud_recording.v1.api_start.RecordingConfig`
        :value: instance of `agora_rest_client.services.cloud_recording.v1.mix_recording.api_start.RecordingConfig`

        :type trace_id: string
        :param trace_id: trace id

        :return: response object ResponseApiStart
        """
        return mix_recording_start(self, resource_id, cname, uid, token, storage_config, recording_config=recording_config, trace_id=trace_id)

    def stop(self, resource_id, sid, cname, uid, async_stop=False, trace_id=None):
        """
        Mix recording stop
        停止云端录制

        :type client: object
        :param client: MixRecordingClient object

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
        return mix_recording_stop(self, resource_id, sid, cname, uid, async_stop=async_stop, trace_id=trace_id)

    def update(self, resource_id, sid, cname, uid, stream_subscribe=None, trace_id=None):
        """
        Mix recording update
        更新云端录制设置

        :type client: object
        :param client: MixRecordingClient object

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

        :type stream_subscribe: object
        :param stream_subscribe: stream subscribe
        :refer: `agora_rest_client.services.cloud_recording.v1.api_update.StreamSubscribe`
        :value: instance of `agora_rest_client.services.cloud_recording.v1.mix_recording.api_update.StreamSubscribe`

        :type trace_id: string
        :param trace_id: trace id

        :return: response object ResponseApiUpdate
        """
        return mix_recording_update(self, resource_id, sid, cname, uid, stream_subscribe=stream_subscribe, trace_id=trace_id)

    def update_layout(self, resource_id, sid, cname, uid, max_resolution_uid=None, mixed_video_layout=None, background_color=None,
                      background_image=None, default_user_background_image=None, layout_config=None, background_config=None, trace_id=None):
        """
        Mix recording update layout
        更新云端录制合流布局

        :type client: object
        :param client: MixRecordingClient object

        :type resource_id: str
        :param resource_id: resource id
        :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.RequestPathParamsApiUpdate.resource_id`

        :type sid: str
        :param sid: sid
        :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.RequestPathParamsApiUpdate.sid`

        :type cname: str
        :param cname: cname
        :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.RequestBodyApiUpdate.cname`

        :type uid: str
        :param uid: uid
        :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.RequestBodyApiUpdate.uid`

        :type max_resolution_uid: str
        :param max_resolution_uid: max resolution uid
        :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.ClientRequest.maxResolutionUid`

        :type mixed_video_layout: int
        :param mixed_video_layout: mixed video layout
        :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.ClientRequest.mixedVideoLayout`

        :type background_color: str
        :param background_color: background color
        :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.ClientRequest.backgroundColor`

        :type background_image: str
        :param background_image: background image
        :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.ClientRequest.backgroundImage`

        :type default_user_background_image: str
        :param default_user_background_image: default user background image
        :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.ClientRequest.defaultUserBackgroundImage`

        :type layout_config: object
        :param layout_config: layout config
        :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.LayoutConfig`
        :value: instance of `agora_rest_client.services.cloud_recording.v1.mix_recording.api_update_layout.LayoutConfig`

        :type background_config: object
        :param background_config: background config
        :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.BackgroundConfig`
        :value: instance of `agora_rest_client.services.cloud_recording.v1.mix_recording.api_update_layout.BackgroundConfig`

        :type trace_id: string
        :param trace_id: trace id

        :return: response object ResponseApiUpdate
        """
        return mix_recording_update_layout(self, resource_id, sid, cname, uid, max_resolution_uid=max_resolution_uid, mixed_video_layout=mixed_video_layout,
                                           background_color=background_color, background_image=background_image, default_user_background_image=default_user_background_image,
                                           layout_config=layout_config, background_config=background_config, trace_id=trace_id)
