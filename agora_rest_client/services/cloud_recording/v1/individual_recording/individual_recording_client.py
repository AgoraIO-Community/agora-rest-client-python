from agora_rest_client.services.cloud_recording.v1.api import SnapshotType
from agora_rest_client.services.cloud_recording.v1.cloud_recording_client import CloudRecordingClient
from agora_rest_client.services.cloud_recording.v1.individual_recording.api_acquire import individual_recording_acquire
from agora_rest_client.services.cloud_recording.v1.individual_recording.api_query import individual_recording_query
from agora_rest_client.services.cloud_recording.v1.individual_recording.api_start import individual_recording_start
from agora_rest_client.services.cloud_recording.v1.individual_recording.api_stop import individual_recording_stop
from agora_rest_client.services.cloud_recording.v1.individual_recording.api_update import individual_recording_update

class IndividualRecordingClient(CloudRecordingClient):
    """
    Individual recording client
    """

    def __init__(self):
        super(IndividualRecordingClient, self).__init__()

    def new_builder():
        return IndividualRecordingClient()

    def acquire(self, cname, uid, enable_postpone_transcoding_mix=False, resource_expired_hour=None, exclude_resource_ids=None, region_affinity=None, trace_id=None):
        """
        Individual recording acquire
        获取云端录制资源

        :type client: object
        :param client: IndividualRecordingClient object

        :type cname: str
        :param cname: cname
        :refer: `agora_rest_client.services.cloud_recording.v1.api_acquire.RequestBodyApiAcquire.cname`

        :type uid: str
        :param uid: uid
        :refer: `agora_rest_client.services.cloud_recording.v1.api_acquire.RequestBodyApiAcquire.uid`

        :type enable_postpone_transcoding_mix: bool
        :param enable_postpone_transcoding_mix: 开启延时转码或延时混音

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
        return individual_recording_acquire(self, cname, uid, enable_postpone_transcoding_mix=enable_postpone_transcoding_mix,
                                            resource_expired_hour=resource_expired_hour, exclude_resource_ids=exclude_resource_ids,
                                            region_affinity=region_affinity, trace_id=trace_id)

    def query(self, resource_id, sid, trace_id=None):
        """
        Individual recording query
        查询云端录制状态

        :type client: object
        :param client: IndividualRecordingClient object

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
        return individual_recording_query(self, resource_id, sid, trace_id=trace_id)

    def start(self, resource_id, cname, uid, token, storage_config, recording_config=None, snapshot_type=SnapshotType.SNAPSHOT_AND_RECORDING.value,
              snapshot_config=None, apps_collection=None, transcode_options=None, trace_id=None):
        """
        Individual recording start
        开始云端录制

        :type client: object
        :param client: IndividualRecordingClientgClient object

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

        :type recording_config: object
        :param recording_config: recording config
        :refer: `agora_rest_client.services.cloud_recording.v1.api_start.RecordingConfig`

        :type snapshot_type: int
        :param snapshot_type: 视频截图类型
        :refer: `agora_rest_client.services.cloud_recording.v1.api.SnapshotType`
        :value: enum of `agora_rest_client.services.cloud_recording.v1.api.SnapshotType`

        :type snapshot_config: object
        :param snapshot_config: snapshot config
        :refer: `agora_rest_client.services.cloud_recording.v1.api_start.SnapshotConfig`
        :value: instance of `agora_rest_client.services.cloud_recording.v1.individual_recording.api_start.SnapshotConfig`

        :type apps_collection: object
        :param apps_collection: apps collection
        :refer: `agora_rest_client.services.cloud_recording.v1.api_start.AppsCollection`
        :value: instance of `agora_rest_client.services.cloud_recording.v1.individual_recording.api_start.AppsCollection`

        :type transcode_options: object
        :param transcode_options: transcode options
        :refer: `agora_rest_client.services.cloud_recording.v1.api_start.TranscodeOptions`
        :value: instance of `agora_rest_client.services.cloud_recording.v1.individual_recording.api_start.TranscodeOptions`

        :type trace_id: string
        :param trace_id: trace id

        :return: response object ResponseApiStart
        """
        return individual_recording_start(self, resource_id, cname, uid, token, storage_config, recording_config=recording_config,
                                          snapshot_type=snapshot_type, snapshot_config=snapshot_config, apps_collection=apps_collection,
                                          transcode_options=transcode_options, trace_id=trace_id)

    def stop(self, resource_id, sid, cname, uid, async_stop=False, trace_id=None):
        """
        Individual recording stop
        停止云端录制

        :type client: object
        :param client: IndividualRecordingClient object

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
        return individual_recording_stop(self, resource_id, sid, cname, uid, async_stop=async_stop, trace_id=trace_id)

    def update(self, resource_id, sid, cname, uid, stream_subscribe=None, trace_id=None):
        """
        Individual recording update
        更新云端录制设置

        :type client: object
        :param client: IndividualRecordingClient object

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
        :value: instance of `agora_rest_client.services.cloud_recording.v1.individual_recording.api_update.StreamSubscribe`

        :type trace_id: string
        :param trace_id: trace id

        :return: response object ResponseApiUpdate
        """
        return individual_recording_update(self, resource_id, sid, cname, uid, stream_subscribe=stream_subscribe, trace_id=trace_id)
